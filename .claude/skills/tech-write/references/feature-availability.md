# Feature Availability Reference

Internal reference for understanding how Visual Layer controls feature availability across the product. Use this when writing documentation, answering support questions, or determining whether a feature should be documented as generally available.

**Product codebase location:** the `vl-product` repository, expected to be cloned alongside this docs repo (e.g., `../vl-product` relative to the VL-documentation root)

All file paths in this document are relative to that root. When verifying feature state, read the actual files at those paths directly. Do not infer behavior from documentation, memory, or grep results alone — the source of truth is the code.

## How It Works

Every feature passes through a **calculator pipeline** before reaching the user. The pipeline evaluates seven layers in order, each able to restrict (but never re-enable) a feature. The final output is one of five behaviors:

| Behavior | What the user sees | What it means for docs |
|----------|-------------------|----------------------|
| **SHOW** | Feature is visible and interactive | Document it — it's available |
| **GREY_OUT** | Feature is visible but disabled, with a reason tooltip | Document it, note the conditions that disable it |
| **HIDE** | Feature is completely invisible | Do NOT document it as available for this audience |
| **TOGGLE** | Feature appears as a toggleable option | Document the toggle behavior |
| **MULTI_SELECT** | _(reserved — not emitted by any calculator)_ | Do not document; defined in `feature_types.py` and `fe/clustplorer/src/types.ts` but unused |

## The Seven Gating Layers

Features are evaluated in this order. Each layer can only restrict further — never re-enable something a previous layer disabled.

### Layer 1: Global + User Settings (Priority 10)

**Where:** `vl/common/settings.py` → `Settings.FEATURE_X_ENABLED`

Base on/off toggle. Set via environment variables, deployment config, or runtime database overrides. Most features default to `true` or `false` here.

**Per-user allowlists** use the pattern `Settings.FEATURE_X_ENABLED_EMAILS` — a list of email addresses that get the feature regardless of the global toggle. The allowlist values in `settings.py` are empty placeholders; the populated lists live in `devops/env/prod/values.yaml`.

### Layer 2: Dataset Flags (Priority 20)

**Where:** `datasets` table → per-dataset boolean columns

Some features require a dataset-level flag set at creation time:

| Flag | Controls |
|------|----------|
| `snapshot_support` | Snapshot create/restore/clone/delete |
| `face_mode_enabled` | Face detection clustering mode |
| `uses_status_v2` | New status system display |

### Layer 2.5: Add Media Tab (Priority 22)

**Where:** `clustplorer/logic/feature_manager/calculators/add_media_tab_calculator.py`

Derives the `ADD_MEDIA_TAB` feature state directly from `ADD_MEDIA` state. `ADD_MEDIA_TAB` controls tab visibility; `ADD_MEDIA` controls the action button. These are separate features. Several task-blocking rules in Layer 4 target `ADD_MEDIA_TAB` specifically, not `ADD_MEDIA`.

### Layer 3: Feature-Specific Logic (Priority 25)

**Where:** `clustplorer/logic/feature_checks.py` and dedicated calculators

Complex multi-condition checks. Example: Flywheel (`feature_checks.py:255–261`) returns `False` unconditionally if `dataset.embedding_config` is `None` — embeddings are required regardless of any flag or allowlist. When embeddings are present, `FLYWHEEL_ENABLED = true` grants access globally. When `FLYWHEEL_ENABLED = false`, users in `FLYWHEEL_ENABLED_EMAILS` still get access — the allowlist bypasses the global toggle entirely.

### Layer 4: Running Tasks (Priority 30)

**Where:** `clustplorer/logic/feature_manager/calculators/task_based_calculator.py`

Features are greyed out while conflicting operations run. Note that `ADD_MEDIA` (the action button) and `ADD_MEDIA_TAB` (the tab visibility) are separate features and are blocked independently.

| Running Task | Features Greyed Out |
|-------------|-------------------|
| Enrichment | `ADD_MEDIA_TAB`, snapshot create/restore |
| Media addition | `ADD_MEDIA`, enrichment, snapshot create/restore |
| Re-index | `ADD_MEDIA`, `ADD_MEDIA_TAB`, enrichment, snapshot create/restore |
| Label propagation | `TRAIN_WORTHY`, train model, `ADD_MEDIA`, `ADD_MEDIA_TAB`, enrichment, snapshot create/restore |
| Training | Train model, enrichment |
| Snapshot restore | Enrichment, `ADD_MEDIA`, `ADD_MEDIA_TAB`, custom metadata, snapshot create/restore |
| Snapshot clone | Nothing (runs on new dataset) |

When a task runs, the dataset status transitions to `READ_ONLY`. This means Layer 4 and Layer 5 fire simultaneously for largely the same features — they are belt-and-suspenders by design, not alternatives. See the Layer 5 note for production implications.

### Layer 5: Dataset Status (Priority 39)

**Where:** `clustplorer/logic/feature_manager/calculators/ds_status_calculator.py`

**Production status:** This calculator only runs when the `NEW_STATUS` feature is currently `SHOW`. `STATUS_NEW_ENABLED` defaults to `false` in `settings.py` and is not overridden in `devops/env/prod/values.yaml`. Layer 5 is therefore inactive in cloud production today. In the meantime, the API auth layer (`validate_dataset_status_for_operation()` in `auth.py`) enforces status-based restrictions at the API boundary independently of the feature manager pipeline. Layer 5 will add UI-level greying on top of that once `STATUS_NEW_ENABLED` is rolled out.

Features are greyed out based on dataset state. `DATASET_SNAPSHOTS_CREATE` and `DATASET_SNAPSHOTS_RESTORE` are tracked as separate features from `DATASET_SNAPSHOTS` (the aggregate); blocking rules target specific operations, not always the aggregate.

| Dataset Status | Disabled Features |
|---------------|------------------|
| **Draft** | Saved views, uniqueness score, add media, `DATASET_SNAPSHOTS_CREATE`, `DATASET_SNAPSHOTS_RESTORE`, flywheel, train model |
| **Indexing** | Saved views, uniqueness score, add media, `DATASET_SNAPSHOTS_CREATE`, `DATASET_SNAPSHOTS_RESTORE`, flywheel, train model, enrichment, custom metadata, delete |
| **Ready** | Everything available |
| **Read Only** | Add media, train model, `DATASET_SNAPSHOTS_CREATE`, custom metadata, uniqueness, flywheel |
| **Partial Index** | Enrichment, flywheel, train model, custom metadata, uniqueness, `DATASET_SNAPSHOTS_CREATE` |
| **Error** | Saved views, uniqueness, enrichment, flywheel, add media, train model, custom metadata |

`READ_ONLY` is the status users encounter most often — it is the state a dataset enters when a task is running (enrichment, add-media, snapshot restore, re-index). This is why Layer 4 and Layer 5 overlap: tasks cause `READ_ONLY`, so both layers target the same features.

### Layer 6: Access Control / OpenFGA (Priority 45)

**Where:** `clustplorer/logic/feature_manager/calculators/access_control_calculator.py`

Greys out features if the user lacks the required permission on the dataset. Key mappings:

| Permission Required | Features |
|--------------------|----------|
| UPDATE | Add media, enrichment, custom metadata, snapshots |
| DELETE | Delete dataset |
| ENRICH | Train model, model validation |
| MANAGE_ACCESS | Share saved views |

This layer **never hides** — only greys out. If a feature is hidden, it was hidden by an earlier layer.

Note: tag operations are enforced at the API auth layer, not in this calculator. There is no `TAGS` entry in the `Features` enum or in `FEATURE_PERMISSION_MAP`. Do not document tags as part of the feature calculator pipeline.

## How to Determine Feature Availability

### Is it live for everyone?

Check `vl/common/settings.py` for `FEATURE_X_ENABLED`. If the default is `true` and there's no restricting allowlist, it may be generally available. Then confirm by reading `devops/env/prod/values.yaml` directly — the prod config is the authority. Do not rely on a cached list of what's enabled; read the file.

### Is it in limited rollout?

Look for the `_EMAILS` suffix pattern in `settings.py`:

```
FEATURE_X_ENABLED = False  ← globally off
FEATURE_X_ENABLED_EMAILS = ["user@company.com"]  ← on for these users
```

When this pattern is present, the feature is in limited rollout. Read `devops/env/prod/values.yaml` to find the actual populated allowlist — `settings.py` contains only empty placeholders.

### Is it not available yet?

Setting defaults to `false`, no email allowlist, not in any environment config.

### Is it staging-only?

Compare environment configs:
- **Staging:** `devops/env/staging/values.yaml`
- **Production:** `devops/env/prod/values.yaml`

Any feature enabled in staging but not production is pre-release. There is also a hardcoded `STAGING_PERMITTED_EMAILS` list in `feature_checks.py` (lines 58–73, 14 entries). The function `is_user_staging_permitted()` at line 240 returns `True` for any VL user OR any email in that list.

### Is it VL-internal only?

`is_vl_user(user)` checks for `@visual-layer.com` email. Internal-only features:
- `SHOW_DS_VERSION` — dataset version debug info
- `ENABLE_DS_DUPLICATE` — dataset duplication
- `EXPLORATION_DEBUG_INFO` — debug console
- Argo pipeline visibility

These are internal tools — do not document for external users.

### Is it on-prem only?

`Settings.RUN_MODE = ONPREM` enables:
- Admin settings API (`/api/v1/admin/settings`)
- User management via Keycloak
- On-prem dataset creation UI (`DATASET_INGESTION_ONPREM_UI_ENABLED`)
- Local folder ingestion
- No JWT auth required

The canonical on-prem config for general customers is `devops/env/k3s/values.yaml` — this is what the K3s installer deploys, and it includes the full feature set (`trainModelEnabled`, `modelsCatalogEnabled`, `FlywheelEnabled`, OIDC, OpenFGA, Longhorn encryption). The OpenShift configs (`devops/env/openshift-prod/`, `devops/env/openshift-staging/`) are for enterprise OpenShift deployments only. The path `devops/env/on-prem/values/features.yaml` is a legacy fragment — do not treat it as the primary on-prem config.

## How to Verify What Is Actually Live

`settings.py` contains fallback defaults only. What runs in cloud production is determined by `devops/env/prod/values.yaml`. Always read that file before drawing any conclusion about availability.

The full resolution chain, from lowest to highest priority:

```
devops/visual-layer/values.yaml           ← Helm chart defaults (lowest priority)
    ↓ overridden by
devops/env/{ENV}/values.yaml              ← Environment-specific values
    ↓ optionally overridden by
devops/clients/{CLIENT}/values.yaml       ← Customer/client overlays (e.g., Camtek)
    ↓ rendered through
devops/visual-layer/templates/config.yaml ← Helm template; maps values → env vars
                                            using {{ .Values.features.X | default "false" | quote }}
    ↓ produces
Kubernetes ConfigMap                      ← Environment variables at runtime
    ↓ read by
vl/common/settings.py                     ← ConfigValue reads env vars; falls back to
                                            hardcoded defaults only when no env var is set
```

Two fallback layers exist below the env config: the Helm template's own `| default` expressions, and then `settings.py` hardcoded defaults. `settings.py` defaults are the last resort, not the authority.

**Populated email allowlists live in `devops/env/prod/values.yaml`, not in `settings.py`.** The `_EMAILS` entries in `settings.py` are empty placeholders. Read the prod config directly to find which external users have been granted access.

## Environment Landscape

Multiple deployment environments exist. Use the right config for the audience you are documenting for.

| Environment | Path | Type | Authoritative for |
|-------------|------|------|-------------------|
| `dev` | `devops/env/dev/` | Cloud (staging cluster) | Developer testing only |
| `staging` | `devops/env/staging/` | Cloud (AWS) | Integration testing |
| `canary` | `devops/env/canary/` | Cloud (prod cluster, prod namespace) | Gradual version rollout; feature flags match prod |
| `prod` | `devops/env/prod/` | Cloud (AWS) | **Cloud production — primary source of truth** |
| `k3s` | `devops/env/k3s/` | On-prem (K3s) | General on-prem customers |
| `k3s-onprem-canary` | `devops/env/k3s-onprem-canary/` | On-prem | On-prem staging |
| `local_openshift` | `devops/env/local_openshift/` | On-prem (local) | Local dev |
| `on-prem` | `devops/env/on-prem/` | On-prem | Enterprise on-prem |
| `openshift-prod` | `devops/env/openshift-prod/` | OpenShift | OpenShift enterprise customers |
| `clients/camtek` | `devops/clients/camtek/` | On-prem (partner overlay) | Camtek-specific overrides on top of K3s/on-prem |

**Canary is not a feature-testing environment.** It runs the same feature flags as `prod` and is used only for gradual version rollout. `prod` and `canary` values should agree; if they differ, flag it.

**For documentation purposes:** cloud user docs → read `devops/env/prod/values.yaml`; general on-prem docs → read `devops/env/k3s/`; Camtek docs → read `devops/clients/camtek/` on top of the base on-prem config.

**Camtek is out of scope for general Visual Layer documentation.** The `devops/clients/camtek/` overlay and any Camtek-specific allowlist entries appear in this reference only to identify what to exclude. Do not surface Camtek features or configs in general docs. Camtek documentation is handled in `vl_camtek` / `vl-docs-camtek` (documentation and code repos) via the `/camtek-docs` skill.

## Infrastructure Prerequisites

Some flags are not part of the seven-layer calculator pipeline but silently disable features that depend on them. A feature can be SHOW in the pipeline and still not function if an infrastructure prerequisite is false.

| Flag | What it gates |
|------|--------------|
| `QUEUE_WORKER_ENABLED` | All async task execution — enrichment, training, label propagation, re-index |
| `VL_ARGO_PIPELINE_ENABLED` | Argo-based pipeline execution; disables features that route through Argo |

Before documenting any async or pipeline-dependent feature, verify these flags in the prod config. If either is false, the feature may be technically enabled in the calculator but non-functional in practice.

## Verifying That a UI Actually Exists

A backend flag set to `true` confirms the feature is enabled in the calculator pipeline. It does not confirm that a frontend component exists or is rendered. Before documenting a UI workflow, verify the frontend separately.

**Step 1:** Find the feature's hook call in the frontend.

```
fe/clustplorer/src/hooks/useFeatureFlagService.ts
```

Search for the feature key (e.g., `ADD_MEDIA`) to confirm the frontend is reading the flag.

**Step 2:** Find the component that renders the UI and confirm it is not behind an additional conditional, a dead code path, or a deployment-specific branch.

**Step 3:** Check `fe/clustplorer/src/contexts/UserConfigContext.tsx` to confirm the feature key is included in the config context the component reads from.

If no component consumes the flag, the feature has no UI regardless of backend state. Document the API only, or do not document at all if there is no API surface either.

## Deployment-Specific UI Routing

A single feature flag can produce entirely different component trees depending on deployment type and secondary flags. Document the UX that applies to the specific deployment type you are writing for — do not assume the cloud UI and the on-prem UI are the same.

Key routing patterns to check before writing any UI procedure:

| Pattern | Where to look | Effect |
|---------|--------------|--------|
| `isOnPremUser()` | `clustplorer/logic/feature_checks.py` | Splits cloud vs. on-prem component paths |
| `DATASET_CREATION_V2` | `settings.py` + prod config | Renders a completely different dataset creation flow |
| `RUN_MODE = ONPREM` | `settings.py` | Enables admin UI, Keycloak user management, local ingestion |
| `DATASET_INGESTION_ONPREM_UI_ENABLED` | `settings.py` | On-prem-specific ingestion interface |

If the user base you are documenting for spans both cloud and on-prem, the procedure must either cover both paths explicitly or state its deployment scope in the opening paragraph.

## Checking Feature State at Runtime

**Authentication:** API calls require cookie-based auth. The browser authenticates using `user_token` and `SESSION` cookies. When running API calls directly, use these cookies from an active browser session — not a Bearer token or API key.

### For a specific user + dataset

Call the user config endpoint:

```
GET /api/v1/user_config?dataset_id=<dataset_id>
```

Response includes:
- `features[]` — each with `feature_key`, `feature_behavior` (SHOW/GREY_OUT/HIDE), `reason`
- `permissions{}` — boolean flags like `can_create_snapshot`, `can_enrich`, `can_export`

### For admin overrides (on-prem only)

```
GET /api/v1/admin/settings?key=FEATURE_X_ENABLED
POST /api/v1/admin/settings  (body: {"key": "FEATURE_X_ENABLED", "value": "true"})
```

Stored in `runtime_settings` PostgreSQL table. Takes effect immediately.

## Documentation Decision Tree

When deciding whether to document a feature, read `devops/env/prod/values.yaml` first — it overrides `settings.py` defaults for everything running in cloud production. `settings.py` shows the last-resort fallback defaults only. If the prod config sets a value, that value is what users actually see.

```
Is FEATURE_X_ENABLED default true in settings.py?
├── YES → Is there an _EMAILS allowlist restricting it?
│   ├── NO → Document as generally available
│   └── YES → Is the allowlist empty or just VL emails?
│       ├── Just VL emails → Do not document (internal testing)
│       └── External emails too → Document with a note about limited availability
└── NO → Is it enabled in production env config?
    ├── YES → Document as generally available (overridden at deployment)
    ├── NO → Is it in staging env config?
    │   ├── YES → Do not document yet (pre-release)
    │   └── NO → Does it have a non-empty _EMAILS allowlist?
    │       ├── NO → Do not document (not shipped)
    │       └── YES → Who is in the allowlist?
    │           ├── Only VL employees (@visual-layer.com)
    │           │   → Internal only. Do not document for any external audience.
    │           ├── One named customer (e.g., Camtek list) AND
    │           │   feature is enabled without restriction in devops/env/k3s/values.yaml
    │           │   → GA for on-prem K3s customers. Document for that audience.
    │           │     Note "not yet available to cloud users" in cloud-facing docs.
    │           ├── One named customer AND not enabled in k3s
    │           │   → Customer-specific. Do not document as general availability.
    │           └── Diverse external users (not one customer)
    │               → Limited rollout / beta. Document only if explicitly instructed.
```

**How to identify the Camtek allowlist:** In `devops/env/prod/values.yaml`, several features share the same email list — Camtek users plus VL employees. When a feature's allowlist matches this pattern AND the same feature is set to `true` with no email restriction in `devops/env/k3s/values.yaml`, it is GA for on-prem and customer-gated for cloud only. Features confirmed in this category include Flywheel, Train Model, Models Catalog, Dataset Creation V2, and Datasets Job Setup Recipe Filters — but always verify against the current configs rather than relying on this list.

## Example: Applying the Decision Tree

Do not maintain a feature inventory here — it goes stale and will mislead. Apply the decision tree each time by reading `settings.py` and the relevant env configs directly.

**Case 1: `DATASET_SNAPSHOTS_ENABLED = true`, no `_EMAILS` allowlist**
GA everywhere. Document as generally available to all users.

**Case 2a: `FLYWHEEL_ENABLED = false`, allowlist contains Camtek users + VL emails, `FlywheelEnabled: true` in `devops/env/k3s/values.yaml`**
GA for on-prem K3s customers. Not yet available to cloud users generally. Document for on-prem audiences. In cloud-facing docs, note that the feature is available to on-prem customers and rolling out to cloud. Do not describe as a general beta.

**Case 2b: `flywheelPreprocessEnabledEmails` contains only two `@visual-layer.com` addresses**
Internal work-in-progress. Do not document for any external audience.

**Case 2c: `STATUS_NEW_ENABLED_EMAILS` contains diverse external users not tied to one customer**
Genuine limited rollout. Document only if explicitly instructed, and note limited availability.

**Case 3: `ENABLE_DS_DUPLICATE` gated by `is_vl_user()` check**
Internal only. Do not document for external users under any circumstances.

## Special Cases

### ENTITY_TYPE_FILTER

`ENTITY_TYPE_FILTER` is the only feature that returns two separate entries in the `GET /api/v1/user_config` response. The `_finalize_features()` method emits it twice: once as `GREY_OUT` for the similarity search context, and once as `TOGGLE` for the general context. No other feature does this. When documenting the user config API response format, note that this feature key appears twice with different behaviors.

## Key Files

| Purpose | Path (relative to vl-product/) |
|---------|-------------------------------|
| All feature flag defaults (fallback only) | `vl/common/settings.py` |
| **Cloud production config (source of truth)** | `devops/env/prod/values.yaml` |
| Canary config (should match prod) | `devops/env/canary/values.yaml` |
| Staging config | `devops/env/staging/values.yaml` |
| General on-prem config (K3s) | `devops/env/k3s/values.yaml` |
| Enterprise on-prem config | `devops/env/on-prem/values.yaml` |
| OpenShift enterprise config | `devops/env/openshift-prod/values.yaml` |
| Camtek client overlay | `devops/clients/camtek/values.yaml` |
| Helm chart defaults (lowest priority) | `devops/visual-layer/values.yaml` |
| Helm template (maps values → env vars) | `devops/visual-layer/templates/config.yaml` |
| Feature check functions | `clustplorer/logic/feature_checks.py` |
| Calculator pipeline | `clustplorer/logic/feature_manager/` |
| Calculator implementations | `clustplorer/logic/feature_manager/calculators/` |
| Feature types enum | `clustplorer/clustplorer_models/feature_types.py` |
| Add media tab calculator | `clustplorer/logic/feature_manager/calculators/add_media_tab_calculator.py` |
| User config endpoint | `clustplorer/web/service.py` |
| Permission mappings | `clustplorer/logic/feature_manager/calculators/access_control_calculator.py` |
| Dataset status rules | `clustplorer/logic/feature_manager/calculators/ds_status_calculator.py` |
| Task blocking rules | `clustplorer/logic/feature_manager/calculators/task_based_calculator.py` |
| API status enforcement (separate from pipeline) | `auth.py` → `validate_dataset_status_for_operation()` |
| Frontend feature hook | `fe/clustplorer/src/hooks/useFeatureFlagService.ts` |
| Frontend config context | `fe/clustplorer/src/contexts/UserConfigContext.tsx` |
| Developer guide | `clustplorer/logic/feature_manager/CLAUDE.md` |

## Confirmed Findings

Items that were previously open questions, now confirmed by direct code audit:

- **`MULTI_SELECT`:** Defined in `FeatureUIBehavior` and `fe/clustplorer/src/types.ts` but not emitted by any calculator. Reserved and unused — do not document.
- **Flywheel allowlist behavior:** Confirmed in `feature_checks.py:255–261`. The allowlist overrides the global toggle: when `FLYWHEEL_ENABLED = false`, users in `FLYWHEEL_ENABLED_EMAILS` receive `True`. The embedding prerequisite fires first and is unconditional.
- **On-prem canonical config:** `devops/env/k3s/values.yaml` is confirmed as the general on-prem customer config. `devops/env/on-prem/` is enterprise on-prem. `devops/env/on-prem/values/features.yaml` is a legacy fragment — do not use it.
