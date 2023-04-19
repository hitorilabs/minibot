# Overview
Building a minimum viable Discord bot. Listen to events and send messages. 

I don't want to see another thousand line Discord bot template out in the wild with too many external dependencies to count. 

A **webhook-based (Interaction Endpoint)** Discord bot in **20 lines of Python**.

For the noobs, check out the wiki page for a [Spelled-out Guide to Your First Discord Bot](https://github.com/hitorilabs/minibot/wiki/Spelled-out-Guide-to-Your-First-Discord-Bot)

For people who might know what's going on, here's what I'm proposing:
- Setup a simple webhook target (`fastapi` Server)
- Setup TCP tunneling to test webhook locally (`cloudflared`)
- Handle Discord Verification for the HTTP API (see [docs](https://discord.com/developers/docs/tutorials/upgrading-to-application-commands#adding-an-interactions-endpoint-url))
  - Handle "PING" event
  - Handle signature validation (use `pynacl`)

You shouldn't take it from me, this guide is based on Discord's documentation.
- [Create an Application](https://discord.com/developers/applications)
- [Interactions Endpoint Verification Process](https://discord.com/developers/docs/tutorials/upgrading-to-application-commands#adding-an-interactions-endpoint-url)
- [Implement Signature Validation](https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization)
- [Registering Commands](https://discord.com/developers/docs/interactions/application-commands#registering-a-command)
- [Interaction Response Format](https://discord.com/developers/docs/interactions/receiving-and-responding#responding-to-an-interaction)

# Other Resources

- `pycord` - if you want to get a bot running with solid DX, async, rate limiting, etc. - then this is your best option. I hope `minibot` helps you appreciate `pycord` a lot more.