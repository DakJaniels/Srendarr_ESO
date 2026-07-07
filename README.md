# SRENDARR: *Advanced Aura Tracking*

![USA](http://icons.iconarchive.com/icons/iconscity/flags/32/usa-icon.png) ![UK](http://icons.iconarchive.com/icons/iconscity/flags/32/uk-icon.png) [![Germany](http://icons.iconarchive.com/icons/iconscity/flags/32/germany-icon.png)](https://translate.google.com/translate?sl=en&tl=de&u=http%3A%2F%2Fwww.esoui.com%2Fdownloads%2Finfo655-Srendarr-AuraBuffampDebuffTracker.html) [![France](http://icons.iconarchive.com/icons/iconscity/flags/32/france-icon.png)](https://translate.google.com/translate?sl=en&tl=fr&u=http%3A%2F%2Fwww.esoui.com%2Fdownloads%2Finfo655-Srendarr-AuraBuffampDebuffTracker.html) [![Russia](http://icons.iconarchive.com/icons/iconscity/flags/32/russia-icon.png)](https://translate.google.com/translate?sl=en&tl=ru&u=http%3A%2F%2Fwww.esoui.com%2Fdownloads%2Finfo655-Srendarr-AuraBuffampDebuffTracker.html) [![Japan](http://icons.iconarchive.com/icons/iconscity/flags/32/japan-icon.png)](https://translate.google.com/translate?sl=en&tl=ja&u=http%3A%2F%2Fwww.esoui.com%2Fdownloads%2Finfo655-Srendarr-AuraBuffampDebuffTracker.html)

*Click your flag to translate the page. Addon includes in-game support for all listed languages.*

## Required libraries

**LibAddonMenu** — [ESOUI](https://www.esoui.com/downloads/info7-LibAddonMenu.html)  
**LibMediaProvider** — [ESOUI](https://www.esoui.com/downloads/info56-LibMediaProvider.html)

### How to add a Prominent Aura

[![How to add a Prominent Aura](https://img.youtube.com/vi/Y9C2lLgv3Cw/hqdefault.jpg)](https://www.youtube.com/watch?v=Y9C2lLgv3Cw)

> **Latest changes:**
>
> **NEW:** Overhauled prominent aura system: Add any aura to any frame!  
> **NEW:** Can now set player buff/debuff, target buff/debuff, and AOE to custom frames by aura or ID!  
> **NEW:** Added the ability to set individual ID's for configured prominent auras to separate frames!

Srendarr replaces the game's limited built-in buff and debuff tracking and gives you the ability to customize the display of these effects on yourself as well as others (even group members). It supports all the standard abilities that appear under the Character window or the built-in tracker, as well as many effects like enchants and gear procs, cooldowns and other things that normally only show via graphical effects on your character (or not at all).

It can also do other things, like keep track of stacks from various abilities like Hawkeye and Merciless Resolve, or from gear like Thrassian Stranglers or Relequin. It also supports display of gear proc cooldowns, and has accurate mechanics for things like collecting the pools from Essence Thief dismissing the proc AOE display, etc.

The aura tracking is designed to visually mesh with the standard UI theme but includes many improvements and options to change the appearance and location of different types of effects.

#### Older description

...and even more options to categorize and filter how the auras appear including multiple movable display windows, groupings for auras of a similar nature, a blacklist for unwanted auras, and now whitelist options for only showing auras you choose on a given frame.

As of version 2.0.0 (and above), S'rendarr uses the API changes made in late 2015 to allow for 'perfect' knowledge about aura details sent directly from the game API. All auras on the player and their target are now displayed and accurate, as is the castbar for the few abilities in game that have a cast time. The downside to this change is the occasional display of 'junk' auras you may not care about. These can be added to the included blacklist (enable debug option to show IDs) or, if you believe the aura should never be displayed, please report its name and when it appeared and it can be included in a 'never show' list built into the mod itself.

![Screenshot](https://i.imgur.com/etDy3WU.jpg) **Track buffs and debuffs on group members!**  
![Screenshot](https://i.imgur.com/Bx25pQn.jpg) **Options** allow either showing only those group buffs/debuffs you care about and specifically whitelist, or to show all group buffs/debuffs except those you blacklist.

![Screenshot](https://i.imgur.com/etDy3WU.jpg) **Separate different effect types into individual frames with their own controls.**  
![Screenshot](https://i.imgur.com/Bx25pQn.jpg) **Filter** options allow sending Short Buffs, Long Buffs, Passives, Toggled Buffs, Proc Cooldowns, Ground AOE, Major/Minor Buffs/Debuffs, Enchant Procs, Debuffs,  
![Screenshot](https://i.imgur.com/Bx25pQn.jpg) **Target** Debuffs, and Target Buffs to their own separate frames, or have multiple types go to the same frames.

![Screenshot](https://i.imgur.com/etDy3WU.jpg) Full customization with *individual frame appearance controls* from Addon Settings.  
![Screenshot](https://i.imgur.com/etDy3WU.jpg) *Assign important effects to specific frames* by name or ability ID, separately for player and target.  
![Screenshot](https://i.imgur.com/etDy3WU.jpg) Option to *only show player-cast debuffs* on targets, and many other filters.  
![Screenshot](https://i.imgur.com/etDy3WU.jpg) *Full debug options* for showing all combat ability IDs in chat and for showing ability ID over active effects.

### v2.4.52 includes *major performance improvements*

> **NEW:** Now supports **Cooldown Tracking** for procs (gear & monster sets) with internal cooldowns!  
> **NEW:** Now supports **Stack Tracking** for abilities and procs with stacks!  
> **NEW:** Now supports **Release Triggers** for abilities and procs with mechanics that cancel timers early (like collecting Essence Thief pools)!
>
> **NEW GROUP BUFF & DEBUFF TRACKING FEATURE**: New in 2.4.19 is the option to show buffs AND debuffs with a duration (configured and shown separately) for everyone in your group or raid on their unit frames. You can either whitelist specific auras to track, or show all buffs/debuffs with a duration that you don't specifically block. Full customization and positioning options, see below video for details.
>
> Group buff & debuff tracking currently supports vanilla, [Foundry Tactical Combat](https://www.esoui.com/downloads/info1611-FoundryTacticalCombatFTC-FoA.html), [Lui Extended](https://www.esoui.com/downloads/info818-LuiExtended.html), [Bandits User Interface](https://www.esoui.com/downloads/info1643-BanditsUserInterface.html), and [AUI](https://www.esoui.com/downloads/info919-AUI-AdvancedUI.html) group & raid frames.

### Slash commands

- `/srendarr unlock` — unlock the aura display for movement
- `/srendarr lock` — relock the display

Additional options can be found in the Settings menu under **Addon Settings → S'rendarr**.

### Debug options

Some new debug options have been added under **Addon Settings → Srendarr** to help track down missing/incorrect auras:

#### Debug option details

- *Enable Display Of Aura's AbilityID* — Set whether to display the internal abilityID of all auras. This can be used to find the exact ID of auras you may want to Blacklist from display or add to the Aura Whitelist display group. This option can also be used to assist in fixing inaccurate aura display by reporting the errant ID's to the addon author.
- *'Show All Combat Events'* — Shows the ID, name, source, and target of every named effect that occurs in combat (both on your character and caused by them), including gear set procs and enchant procs which add a buff effect (but which don't necessarily show on your character sheet for Srendarr to pick up automatically).
- *'Disable Flood Control'* — By default, events will only show once until a reload (to prevent chat spam), however **you can type `/sdbclear` at any time** to reset the debug memory. Enabling this option however will turn off the flood filter entirely, allowing events to show multiple times.
- *'Allow Manual Debug Edit'* — The option lets you type `/sdbadd XXXXXX` or `/sdbremove XXXXXX` (where XXXXXX is the number of an ID you wish to hide/show) to add/remove ID's from the flood filter. You can turn the above on to show everything and then manually blacklist just the specific events you aren't interested in, letting others show multiple times.
- *'Show Verbose Debug'* — Shows the entire data block returned for `EVENT_COMBAT_EVENT`, formatted in a human-readable way.
- *'Show Nameless Events'* — When enabled, Show All Combat Events will also show events with no name as well.
- *Only Player Events* — Only show debug combat events that are the result of player actions.

- `/sdbclear` — Clears the current flood filter.
- `/sdbadd` — Adds a single ID to the flood filter so it is no longer shown (must enable manual debug option).
- `/sdbremove` — Remove a single ID from the flood filter.
- `/sdbignore` — Add a single ID to the ignore list for the flood filter (always shows).

### Future plans

- ~~Migrate saved variables to new character ID format (preserves settings when renaming).~~ Done.
- ~~Implement new API-supported event filters for EVENT_COMBAT_EVENT to significantly improve performance.~~ Done.
- Fix any changes/issues with gear set proc tracking and add new sets as needed. (Current as of 10-1-2021).
- Continually monitor whether unique event data needed for target nameplate anchoring becomes available in API.
- Continued updates of Major/Minor buff/debuff sources & code/bug fixes. (Current as of 11-28-2021).
- Investigate possible new features.

### Bugs & feedback

Please use the [Author Portal](http://www.esoui.com/portal.php?uid=2720) to report [Bugs](http://www.esoui.com/portal.php?uid=2720&a=listbugs) and [Features](http://www.esoui.com/portal.php?uid=2720&a=listfeatures).

[![Group buff tracking](https://img.youtube.com/vi/uFHQs5Dalko/hqdefault.jpg)](https://www.youtube.com/watch?v=uFHQs5Dalko)  
*[Update option info](https://www.youtube.com/watch?v=mZcn6Vv_074)*

[![Video](https://img.youtube.com/vi/fL6BRYOUBcg/hqdefault.jpg)](https://www.youtube.com/watch?v=fL6BRYOUBcg)

**[Check out this helpful configuration tutorial from Yolo Wizard!](http://www.youtube.com/watch?v=XGmXYsnnybs)**

[![Screenshot](http://i.imgur.com/dA6XnHQ.jpg)](http://i.imgur.com/oME6IkY.jpg)

I wanted to share my gratitude and appreciation for the excellent players who came together to help me through vMoL. Raiding and PVP haven't really been an option for me since my brain cavernoma, but these kind folks helped me through it and what's more, it was a blast hanging out and chatting with them! Thanks @nekotakoyaki, @anotherTimeWizard, @Sneebly, @Dr'Strange, @YuYJ, @Rossdresser, @HalfEatenCornea, @MrPickel, @FKNSTEVO, @iTz_RickDawg, and @stileanima for the help and humor and good times, and the awesome Dro-m'Athra skin of course!

View [my other addons on ESOUI](http://www.esoui.com/downloads/author-2720.html).
