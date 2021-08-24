# Perk.Exchange GitHub Action

Reward developers and users with cryptocurrency for performing certain actions. Rewards are provisioned by <https://perk.exchange>.

## Get Access

We are in the test phase of this action. Please reach out to us on Twitter for early access:

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/perkexchange.svg?style=social&label=Perk.Exchange)](https://twitter.com/perkexchange)

## Usage

Copy the example workflow below

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  reward:
    runs-on: ubuntu-latest

    steps:
        # Reward the initiating user with cryptocurrency       
      - uses: perkexchange/github-action@v0.3
        name: Perk.Exchange Reward
        with:
            apiToken: XXXXXXXXXXX
            campaignReference: YYYYYYYYYYY
            userId: ${{ github.event.sender.id }}
            amount: 3
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `apiToken`  | Perk.Exchange developer API token. Once enabled, available here: https://perk.exchange/Developer    |
| `campaignReference`  | A reference that uniquely identifies your campaign (Perk)    |
| `userId`  | The user's internal Id    |
| `amount`  | Reward amount   |
| `platform` _(optional)_  | User platform: github (default), twitter, github, google, slack, discord    |

### Outputs

None

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!
