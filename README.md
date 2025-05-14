# Prerequisites

Before you start, ensure you have the following installed:

- **Git**: [Download Git](https://git-scm.com/) (for version control)
- **Node.js**: [Download Node.js](https://nodejs.org/) (LTS version recommended)
- **A GitHub account**
- **A code editor**: e.g., [Visual Studio Code](https://code.visualstudio.com/)

## Setting Up Your Local Environment

### 🛠️ Installing the Mintlify CLI

#### Step 1: Ensure Node.js is Installed
Mintlify CLI requires **Node.js version 19 or higher**.

- **Check your current version**:
    ```bash
    node -v
    ```
- **If needed, install or upgrade Node.js**:
    - Using Node Version Manager (nvm):
        ```bash
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
        nvm install node
        ```
    - Direct download: Visit the [official Node.js website](https://nodejs.org/) and download the latest version.

#### Step 2: Install the Mintlify CLI Globally
Install via npm:
```bash
npm install -g mintlify
```
This command installs the Mintlify CLI globally, allowing you to use it from any directory.

#### Step 3: Verify the Installation
Check the installed version:
```bash
mintlify --version
```
This ensures that the CLI is installed correctly and is accessible from your terminal.

### 🚀 Using the Mintlify CLI in Your Workflow

#### Preview Documentation Locally
1. Navigate to your project directory (ensure it contains the `docs.json` file).
2. Run the development server:
     ```bash
     mintlify dev
     ```
3. Open your browser and visit `http://localhost:3000` to view your documentation.

#### Customize the Development Server Port
If port 3000 is in use or you prefer a different port:
```bash
mintlify dev --port 3333
```
This starts the server on port 3333.