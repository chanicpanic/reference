
.. include:: <isopub.txt>

.. |copy| unicode:: 0xA9 .. copyright sign
.. |tm| unicode:: U+2122

How to Play
###########

Summary of Gameplay
*******************

During the first two rounds, players establish their defenses by playing health
and shield cards. Beginning round 3, attacking is allowed, and players can begin
to chip away at their opponents' defenses or eliminate them entirely. If you survive
until round 4, you can unleash the Shield Bypass, a special attack that renders
an opponent's shields useless. All of this is while ensuring you are protecting 
yourself while leveraging abilities, resource cards, and alliances. If you
are the last man standing, you are the winner.

The Board
*********

Each player has a personal board on which to play Utility Cards. The board 
consists of 9 slots -- 3 for each of Hearts, Diamonds, or Spades. Hearts are 
placed in a row closest to the player, Spades furthest away, and Diamonds in 
the middle. **Important**: There may be no more than 3 cards of the same suit
on a player's board at the same time.

The Deck
********

Chanic Panic uses a standard deck of cards. However, face cards are not used.
In other words, Jacks, Queens, and Kings are removed from the deck. 

All players share the same deck.

Within the game, the cards are placed into two groups based on their suit.

Utility Cards
=============

These are cards that are be played on the board. This includes Hearts, Diamonds,
and Spades.

Hearts
------

Hearts represent Health. If a player's health becomes 0 or less as a result of
an attack, that player is eliminated from the game.

Diamonds
--------

Diamonds represent Shields. A player must destroy all Diamond cards of another
player before being able to attack their Hearts with full power.

Spades
------

Spades represent Weapons. They are used to attack and destroy Heart and Diamond
cards, ultimately winning the game. They may not be played until round 3.

Resource Cards
==============

These are cards that increase drawing and playing power. They consist of Clubs.
Unlike Utility Cards, they are not played on the board. They are discarded
after use.

Clubs
-----

The mechanics of the Club are explained later_ to reduce confusion.

Card Attributes
===============

Here attributes of cards are listed. They should be thoroughly understood.

Base Value
==========

This is the number on a card. 

.. note:: Aces have a Base Value of 1.

   *Reminder*: There are no face cards.

(Effective) Value
=================

This is the resulting value after applying modifiers to a card's Base Value.
For the purposes of the most basic version of the game, this is always
equal to a card's Base Value. However, when playing with special abilities or
other variants, this is an important distinction that must be made.

Cost
----

This attribute **only** applies to Utility Cards. This is the number of Points 
required to play a Utility Card. The vast majority of the time, it is equal
to a card's Base Value.

Taking a Turn
*************

Phases
======

The Turn is broken up into 3 phases in which different actions are taken or
available.

1. Draw Phase
-------------

During the first round, a player draws 5 cards from the top of the deck, as
players start with 0 cards in hand. On all following turns in rounds 2 and 
beyond, a player draws 1 card.

2. Point Phase
--------------

After Drawing, a player moves into the Point Phase. At the beginning of the
Point Phase, a player gets 12 Points. Points are the unit of Cost, and are used
to play Utility Cards. So, for example playing 8\ |diams| costs 8 points,
leaving the player with 4 Points to spend on other Utility Cards. Points are
not carried over from turn to turn. Any unused Points are lost.  Any number of
Utility Cards may be played during the Point Phase with the only limits being
the number of Points and the number of open slots on the board. *Reminder*:
Spades cannot be played until Round 3.

3. Club Phase
-------------

The Club Phase is an optional phase that follows the Point Phase. The Club Phase
begins as soon as a player plays a Club for the first time during the turn. A
player may choose to play a Club at any time during the Point Phase.
As soon as the Club Phase begins, all Points are lost, and Points are irrelevant
for the remainder of the turn.

Club Mechanics
^^^^^^^^^^^^^^

The mechanics of Clubs may be confusing to some, so take care to understand them.

When played, a Club is placed on the top of the discard pile. A Club has two
effects: The first is mandatory, and the other optional.

1. Draw.

   If the Base Value of the Club is:

   * 1-5: draw 2 cards.
   * 6-10: draw 1 card.

2. Play one card with a Base Value less than or equal to the Value of the Club.

For example, a player plays a 5\ |clubs|\. The Club is placed on the discard
pile, and the player draws 2 cards. The player then plays a 5\ |hearts|\.
At this point, the player's options are limited, as no more cards can be 
played. The player proceeds to end his turn.

It is valid to take other actions between resolving the first effect of a Club
and using its second. 

Club Chaining
"""""""""""""

It is perfectly legal to play a Club after playing a Club as long as its
Value is less than or equal to the Value of the former. This allows a player
to play more Clubs and obtain more cards.

Attacking
=========

Fundamentals
------------

* Attacking is the action of using Spades one controls on the board to destroy the Diamonds
  and Hearts of on an opponent's board.
* As Spades cannot be played until round 3, a player may not attack until round
  3.
* The only way to attack is with Spades.
* A player may only attack if he can destroy at least one Diamond or Heart 
  Card of an opponent.
* A player is never required to attack.
* All Diamond cards of an opponent must be destroyed before attacking their
  Hearts with full damage.
* To destroy a card, any combination of Spade Values must be greater than or 
  equal to any combination of an opponent's Diamond or Heart values.

Examples
^^^^^^^^

Cannot Destroy:

* 6\ |spades| vs. 7\ |diams|
* 3\ |spades| + 2\ |spades| vs. 6\ |diams|

Can Destroy:

* 6\ |spades| vs. 6\ |diams|
* 5\ |spades| vs. 4\ |diams|
* 6\ |spades| vs. 4\ |diams| + 2\ |diams|
* 8\ |spades| vs. 3\ |diams| + 2\ |diams|
* 5\ |spades| + 4\ |spades| vs. 8\ |diams|
* 6\ |spades| + A\ |spades| vs. 7\ |diams|
* 7\ |spades| + 3\ |spades| vs. 6\ |diams| + 4\ |diams|
* 6\ |spades| + 5\ |spades| vs. 7\ |diams| + 2\ |diams|
* 7\ |spades| vs. 4\ |diams| vs. 2\ |diams| + A\ |diams|

**Note**: All Diamonds in the above examples can be replaced with Hearts assuming
the opponent has no diamonds on the board, or the last Diamond is destroyed in
the attack.

The Shield Bypass
-----------------

Beginning round 4, players are allowed to perform a special attack called the
Shield Bypass. With this attack, a player attacks an opponent's Hearts directly,
ignoring any shields. However, attack power is cut in half and rounded down.

For example, if an opponent's board is: 

| |hearts| 4 6
| |diams|  8 7 2
| |spades| 3

A player could use an 8\ |spades| to destroy the 4\ |hearts|. A player
could also use 7\ |spades| + 6\ |spades| to destroy the 6\ |hearts|.

Attack Resolution
-----------------

After an attack, all Spades used, and all Diamonds and Hearts destroyed are
sent to the discard pile.

Additional Rules
================

* A player may not be attacked by more than two different players before having
  another turn.

Abilities
*********

Abilities are special actions that players can use to their advantage.

All players have the following ability.

*Trader*
  Discard 2 cards: Draw 1 card.

*Trader* can be used during the Point and Club Phases as many times as possible.

You can also play with the following optional ability for all players.

*Panic*
  Once per game: Discard all Spades you own: Discard all Spades your next
  opponent controls; End your turn; You may not be attacked until the end of
  your next turn.

For more details on the above abilities see the Ability Reference.

Special Abilities
=================

Beside those listed above, there are several unique special abilities that
can be used. This greatly expands the base game. For details, see
Playing with Abilities.

Ending the Game
***************

Elimination
===========

A player is eliminated when is Health is 0 or less as a result of an attack.
All of an eliminated player's cards on the board and the hand go to the discard
pile.

Special Cases:

Winning the Game
================

A player wins the game when all opponents have been eliminated.

Additional Rules and Notes
**************************

* Full Hand: A Full Hand is 8 cards. A player may never hold more than a Full
  Hand. That is, a player skips drawing if holding a Full Hand.
* When the deck is exhausted, the discard pile is shuffled and becomes the deck.
* Generally, the player with the least experience, or the player who was 
  eliminated first in the previous game takes the first turn. Play continues
  clockwise.
* For every 2 players, one deck should be used rounded up. So, if there are
  4 players, 2 decks are used. If there are 5 players, 3 decks are used.

More Ways to Play
*****************

Congratulations, you now know Chanic Panic fundamentals. Play with your friends
and tune your skills. When you are ready, there are many ways to keep your 
Chanic Panic experience fresh and exciting.

* Playing in Large Groups
* Using Special Abilities
* Presence
* The Stack
* The Shop
* Lives

.. _later: `Club Mechanics`_
