# Overview
Building a minimum viable Discord bot. In this case, we consider a "bot" to be anything that can listen for things that happen in Discord and respond back.

I don't want to see another thousand line Discord bot template out in the wild with too many external dependencies to count. Here are the fundamental building blocks of a webhook-based (Interaction Endpoint) Discord bot in 30 lines of Python.

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

## Interaction Create Gateway Event (Gateway API) vs. Outgoing Webhook (HTTP API)
These two methods are mutually exclusive; you can only receive Interactions one of the two ways. The INTERACTION_CREATE Gateway Event may be handled by connected clients, while the webhook method detailed below does not require a connected client.

- The Gateway API lets apps open secure WebSocket connections with Discord to receive events 
- The Interactions Endpoint is a regular HTTP API webhook

Not all applications have a use case for WebSockets, but you'll know when you need it. Out of scope for this repository.

## The Beauty of Discord's Webhook Verification

Normally, you can easily shoot yourself in the foot if you don't implement signature validation. Most apps don't even bother to stop you, but Discord actually cared enough to protect you.

- Your endpoint must be prepared to ACK a PING message
- Your endpoint must be set up to properly handle signature headers--more on that in Security and Authorization

## Bots vs. Users

Bot accounts have a few differences in comparison to normal user accounts, namely:

- Bots are added to guilds through the OAuth2 API, and cannot accept normal invites.
- Bots cannot have friends, nor be added to or join Group DMs.
- Verified bots do not have a maximum number of Guilds.
- Bots have an entirely separate set of Rate Limits.
