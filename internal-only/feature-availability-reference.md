# Feature Availability Reference

Internal reference for understanding how Visual Layer controls feature availability across the product. Use this when writing documentation, answering support questions, or determining whether a feature should be documented as generally available.

## How It Works

Every feature passes through a **calculator pipeline** before reaching the user. The pipeline evaluates six layers in order, each able to restrict (but never re-enable) a feature. The final output is one of four behaviors:

| Behavior | What the user sees | What it means for docs |
|----------|-------------------|----------------------|
| **SHOW** | Feature is visible and interactive | Document it — it's available |
| **GREY_OUT** | Feature is visible but disabled, with a reason tooltip | Document it, note the conditions that disable it |
| **HIDE** | Feature is completely invisible | Do NOT document it as available for this audience |
| **TOGGLE** | Feature appears as a toggleable option | Document the toggle behavior |

## The Six Gating Layers

Features are evaluated in this order. Each layer can only restrict further — never re-enable something a previous layer disabled.

### Layer 1: Global + User Settings (Priority 10)

**Where:** `vl/common/settings.py` → `Settings.FEATURE_X_ENABLED`

Base on/off toggle. Set via environment variables, deployment config, or runtime database overrides. Most features default to `true` or `false` here.

**Per-user allowlists** use the pattern `Settings.FEATURE_X_ENABLED_EMAILS` — a list of email addresses that get the feature regardless of the global toggle.

### Layer 2: Dataset Flags (Priority 20)

**Where:** `datasets` table → per-dataset boolean columns

Some features require a dataset-level flag set at creation time:

| Flag | Controls |
|------|----------|
| `snapshot_support` | Snapshot create/restore/clone/delete |
| `face_mode_enabled` | Face detection clustering mode |
| `uses_status_v2` | New status system display |

### Layer 3: Feature-Specific Logic (Priority 25)

**Where:** `clustplorer/logic/feature_checks.py` and dedicated calculators

Complex multi-condition checks. Example: Flywheel requires `Settings.FLYWHEEL_ENABLED` OR user email in allowlist, AND dataset must have compatible embeddings.

### Layer 4: Running Tasks (Priority 30)

**Where:** `clustplorer/logic/feature_manager/calculators/task_based_calculator.py`

Features are greyed out while conflicting operations run:

| Running Task | Features Greyed Out |
|-------------|-------------------|
| Enrichment | Add media, snapshot create/restore |
| Media addition | Add media, enrichment, snapshot create/restore |
| Re-index | Add media, enrichment, snapshot create/restore |
| Label propagation | Train model, add media, enrichment, snapshots |
| Training | Train model, enrichment |
| Snapshot restore | Enrichment, add media, custom metadata, snapshot create/restore |
| Snapshot clone | Nothing (runs on new dataset) |

### Layer 5: Dataset Status (Priority 39)

**Where:** `clustplorer/logic/feature_manager/calculators/ds_status_calculator.py`

Features are greyed out based on dataset state:

| Dataset Status | Disabled Features |
|---------------|------------------|
| **Draft** | Saved views, uniqueness score, add media, snapshots, flywheel, train model |
| **Indexing** | All of Draft + enrichment, custom metadata, delete |
| **Ready** | Everything available |
| **Read Only** | Add media, train model, snapshots create, custom metadata, uniqueness, flywheel |
| **Partial Index** | Enrichment, flywheel, train model, custom metadata, uniqueness, snapshots create |
| **Error** | Saved views, uniqueness, enrichment, flywheel, add media, train model, custom metadata |

### Layer 6: Access Control / OpenFGA (Priority 45)

**Where:** `clustplorer/logic/feature_manager/calculators/access_control_calculator.py`

Greys out features if the user lacks the required permission on the dataset. Key mappings:

| Permission Required | Features |
|--------------------|----------|
| UPDATE | Add media, enrichment, custom metadata, snapshots, tags |
| DELETE | Delete dataset |
| ENRICH | Train model, model validation |
| MANAGE_ACCESS | Share saved views |

This layer **never hides** — only greys out. If a feature is hidden, it was hidden by an earlier layer.

## How to Determine Feature Availability

### Is it live for everyone?

Check `vl/common/settings.py` for `FEATURE_X_ENABLED`. If the default is `true` and there's no restricting allowlist, it's generally available.

**Currently GA features** (default enabled, no allowlist gating):
- Dataset snapshots (`DATASET_SNAPSHOTS_ENABLED = true`)
- Dataset sharing (`DATASET_SHARE_ENABLED = true`)
- VQL upgrade (`VQL_UPGRADE_ENABLED = true`)
- Cluster by duplicates (`CLUSTER_BY_DUPLICATES_ENABLED = true`)
- Uniqueness score (`UNIQUENESS_SCORE_ENABLED = true`)
- Saved views, export, search, explore — all on by default
- VL Chat (`VL_CHAT_ENABLED`) — check current setting

### Is it in limited rollout?

Look for the `_EMAILS` suffix pattern in `settings.py`:

```
FEATURE_X_ENABLED = False  ← globally off
FEATURE_X_ENABLED_EMAILS = ["user@company.com"]  ← on for these users
```

**Known limited-rollout features** (have email allowlists):
- Flywheel / Label Propagation (`FLYWHEEL_ENABLED` + `FLYWHEEL_ENABLED_EMAILS`)
- Enrichment inline flow (`ENRICHMENT_INLINE_FLOW_ENABLED` + `ENRICHMENT_INLINE_FLOW_ENABLED_EMAILS`)
- Dataset creation v2 (`DATASET_CREATION_V2` + `DATASET_CREATION_V2_ENABLED_EMAILS`)
- VL Chat debug console (`VL_CHAT_DEBUG_CONSOLE_ENABLED_EMAILS`)

### Is it not available yet?

Setting defaults to `false`, no email allowlist, not in any environment config.

### Is it staging-only?

Compare environment configs:
- **Staging:** `devops/env/openshift-staging/values/features.yaml`
- **Production:** `devops/env/openshift-prod/values/features.yaml`

Any feature enabled in staging but not production is pre-release. There's also a hardcoded `STAGING_PERMITTED_EMAILS` list in `feature_checks.py` (~15 emails) that grants staging access to non-VL users.

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

## Checking Feature State at Runtime

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

When deciding whether to document a feature:

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
    │   └── NO → Do not document (not shipped)
    └── Check: does it have a non-empty _EMAILS allowlist?
        └── YES → Feature is in private beta; document only if told to
```

## Key Files

| Purpose | Path (relative to vl-product/) |
|---------|-------------------------------|
| All feature flag defaults | `vl/common/settings.py` |
| Feature check functions | `clustplorer/logic/feature_checks.py` |
| Calculator pipeline | `clustplorer/logic/feature_manager/` |
| Calculator implementations | `clustplorer/logic/feature_manager/calculators/` |
| Feature types enum (all 64) | `clustplorer/clustplorer_models/feature_types.py` |
| User config endpoint | `clustplorer/web/service.py` |
| Permission mappings | `clustplorer/logic/feature_manager/calculators/access_control_calculator.py` |
| Dataset status rules | `clustplorer/logic/feature_manager/calculators/ds_status_calculator.py` |
| Task blocking rules | `clustplorer/logic/feature_manager/calculators/task_based_calculator.py` |
| Staging env config | `devops/env/openshift-staging/values/features.yaml` |
| Production env config | `devops/env/openshift-prod/values/features.yaml` |
| On-prem env config | `devops/env/on-prem/values/features.yaml` |
| Frontend feature hook | `fe/clustplorer/src/hooks/useFeatureFlagService.ts` |
| Frontend config context | `fe/clustplorer/src/contexts/UserConfigContext.tsx` |
| Developer guide | `clustplorer/logic/feature_manager/CLAUDE.md` |

## Feature Inventory Snapshot

Last verified: 2026-03-29

| Feature | Global Default | Allowlist? | Doc Status |
|---------|---------------|-----------|------------|
| Dataset Snapshots | Enabled | No | Documented (UI + API) |
| Saved Views | Enabled | No | Documented (UI + API) |
| Dataset Sharing | Enabled | No | Documented (UI + API) |
| VL Chat | Check setting | No | Documented (UI) |
| Enrichment | Enabled | Inline flow has allowlist | Documented (UI + API) |
| Export | Enabled | No | Documented (UI + API) |
| Visual Search | Enabled | No | Documented (UI + API) |
| Semantic Search | Enabled | No | Documented (UI + API) |
| Tags | Enabled | No | Documented (UI) |
| Task Manager | Enabled | No | Documented (UI + API) |
| Notifications | Enabled | No | Partially documented |
| Custom Metadata | Enabled | No | Documented (API guide) |
| VQL | Enabled | Upgrade has allowlist | Partially documented |
| Flywheel / Label Propagation | **Disabled** | **Yes** | **Not documented** |
| Model Training | Check setting | Has allowlist | **Not documented** |
| Model Validation | Check setting | No | **Not documented** |
| Model Catalog (CRUD) | Enabled | No | Partially documented |
| Workspace Management | Enabled (on-prem w/ auth) | No | **Not documented** |
| User Management (Keycloak) | On-prem only | No | Partially documented |
| Dataset Duplication | **VL-internal only** | No | Do not document |
| Face Mode | Enabled | No | Not documented (niche) |
