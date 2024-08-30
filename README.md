# Perk.Exchange GitHub Action

Reward developers and users with cryptocurrency for performing certain actions. Rewards are provisioned by <https://perk.exchange>.

## Requirements

- **Enable access** We are in the test phase of this action. Please reach out to us on [Twitter](https://twitter.com/perkexchange) for access.

- **Users Register with Perk.Exchange** Users must first connect to https://perk.exchange with their GitHub user. Rewards are not provisioned for GitHub users that haven't already registered with Perk.Exchange.

## Usage

Store your Perk.Exchange **Campaign secret** in a repository secret. Use the example workflow below as a base and modify to suit your needs. You can also refer to this repository's workflow.

**IMPORTANT**: Secrets are not passed to workflows that are triggered by a pull request from a fork. https://docs.github.com/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets

### Example workflow

```yaml
name: My Workflow
on:
  pull_request:
    types: [ closed ]
jobs:
  reward:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest

    steps:
        # Create donation button for this PR
      - uses: perkexchange/github-action@v0.15-alpha
        name: Perk.Exchange Donation Button
        with:
            apiToken: ${{ secrets.PERKEXCHANGE_APITOKEN }}
            currency: "USD"
            amount: 1

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `apiToken`  | Integration api token - Store in a repo secret |
| `amount`  _(optional)_ | Donation amount (default is 1)  |
| `currency` _(optional)_  | Currency (default is "USD")    |
| `orderId` _(optional)_  | Unique donation identifier (default = "{owner}/{repo}/{branch}")    |
| `memo` _(optional)_  | Donation memo (default includes {repo_name} and {pr_url})    |

### Outputs

None

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!

## Sponsorship

Please DM us on [X](https://x.com/perkexchange) for more details.
