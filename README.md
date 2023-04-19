# Overview
Building a minimum viable Discord bot.

In this case, we consider a "bot" to be anything that can listen for things that happen in Discord and respond back.

Check out the wiki page for a [Spelled-out Guide to Your First Discord Bot](https://github.com/hitorilabs/minibot/wiki/Spelled-out-Guide-to-Your-First-Discord-Bot)

---
# FAQ
## Plain Webhooks 
I wouldn't touch this feature with a 10-foot pole. This is what we call a "target" webhook - imagine this is a "bot

If you implement some automated process to provision and immediately revoke or rotate the webhook URL on your server - it would be usable, but you definitely don't want this webhook sitting around.

## Applications

When a user interacts with your app, your app will receive an Interaction. Your app can receive an interaction in one of two ways:

1. Interaction Create Gateway Event
2. Outgoing Webhook


These two methods are mutually exclusive; you can only receive Interactions one of the two ways. The INTERACTION_CREATE Gateway Event may be handled by connected clients, while the webhook method detailed below does not require a connected client.

In your application in the Developer Portal, there is a field on the main page called "Interactions Endpoint URL". If you want to receive Interactions via outgoing webhook, you can set your URL in this field. In order for the URL to be valid, you must be prepared for two things ahead of time:

- Your endpoint must be prepared to ACK a PING message
- Your endpoint must be set up to properly handle signature headers--more on that in Security and Authorization


[Discord Docs](https://discord.com/developers/docs/topics/oauth2#bots)

- Discord's API provides a separate type of user account dedicated to automation
- Bot accounts can be created through the applications page, and are authenticated using a token (rather than a username and password) [...]
- Unlike the normal OAuth2 flow, bot accounts have full access to most API routes without using bearer tokens, and can connect to the Real Time Gateway. Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden, and can result in account termination if found.

Bot accounts have a few differences in comparison to normal user accounts, namely:

- Bots are added to guilds through the OAuth2 API, and cannot accept normal invites.
- Bots cannot have friends, nor be added to or join Group DMs.
- Verified bots do not have a maximum number of Guilds.
- Bots have an entirely separate set of Rate Limits.
