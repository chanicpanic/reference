
Ability Reference
#################

Using this Document
*******************

This document describes in detail different abilities, their effects, usage,
and nuances. Great care has been taken to make the mechanics and descriptions
of abilities as precise as possible. This reference should be the final
word on any disputes in the function of an ability. This guide should be
used in tandem with the glossary, which provides precise definitions of
many terms used in ability descriptions. If you find anything ambiguous
or confusing, or to change, do not hesitate to contact me.

Classifying Abilities
*********************

Base vs. Special
================

There are two categories of Abilities, Base Abilities and Special Abilities.
All players in a game have Base Abilities while unique Special Abilities are
distributed at the beginning of the game.

Passive vs. Active
==================

There are two kinds of Abilities, Passive and Active. Passive abilities are
either always in effect, or activate when a certain condition is satisfied.
Active abilities need to be activated by a player and generally have
a temporary effect.

Using Abilities
***************

- Active abilities may be used during one's Point Phase or Club Phase, 
  unless otherwise specified.
- Any ability that involves Points may only activate during the Point Phase.
- Any ability that involves the Draw Phase does not activate the first turn.
- Abilities may be activated when the required event occurs.
- All events, costs, and conditions must be satisfied for an ability to
  activate.
- An ability may not be activated if one of its effects in unresolved.
- An ability may not be activated while another ability is unresolved at a
  semicolon.

Understanding Abilities
***********************

*Example*:


Syntax
======

The Colon (:)  
-------------

A colon is preceded by one of the following:

- An Event (when, during, at the start, before)
- A Usage Restriction (once per turn, once per game)
- A Cost (discard, pay, skip)

If the conditions preceding a colon are not satisfied, an ability's 
activation fails.

The Semicolon (;)
-----------------

The semicolon separates effect components and indicates that the effect is
not fully resolved.

The Period (.)
--------------

The period indicates the end of an ability's effect.

Base Abilities
**************

.. ability::
   :name: Ally
   :classification: A
   :effect: Give 1 card from your hand to a teammate.
   :rulings: This is a base ability that is available for team games. This 
    ability is useable a number of times equal to half of the number of
    active (not eliminated) players on your team rounded down. Ex. There 
    are 5 players on your team (including yourself). You may give up to
    2 cards this turn as 5/2 = 2.5 which rounds down to 2. You may give
    up to one card to any single teammate. You may not give a card to a 
    teammate who holds a full hand.

.. ability::
   :name: Panic
   :classification: A
   :effect: Once per game: Discard all Spades you own: Discard all Spades
    your next opponent controls; End your turn; You may not be attacked 
    until the end of your next turn.
   :rulings: This is the signature base ability with a one-time effect.
    Your next opponent is defined as the first opponent who will take a
    turn after you.
    It requires that you rid yourself of offensive capabilities in order
    to protect yourself. It can also be used cooperatively to reduce the
    attack power of an opponent who may be able to eliminate a teammate.

.. ability::
   :name: Trader
   :classification: A
   :effect: Discard 2 cards: Draw 1 card.
   :rulings: This base ability provides all players a way to improve the
    hand.

Special Abilities
*****************

.. ability::
   :name: Archaeologist
   :classification: A
   :effect: Once per turn: Pay 4 points: Declare a suit; Discard the top
    card of the deck until a card of the declared suit is discarded or
    the deck runs out; Add the top card of the discard pile to your hand.
   :rulings: This is an effective ability to get the cards you need. If
    the deck runs out, the top card of the discard pile is added to your
    hand before the discard pile is shuffled into the deck.

.. ability::
   :name: Assets
   :classification: P
   :effect: At the start of your Point Phase: Gain 1 Point for every 2 cards
    in your hand.
   :rulings: This ability works well as the more cards you have in your 
    hand, the more you can play, so the more points, the better. Always
    round down. So, having 7 cards would give you 3 points.

.. ability::
   :name: Bargainer
   :classification: P
   :effect: When you use the Trader ability: Gain 2 points.
   :rulings: This adds a nice bonus to your base ability. You have the 
    opportunity to get a better cards and more points in the process. You
    only gain points if the Trader ability is used during the Point Phase.

.. ability::
   :name: Blessed
   :classification: P
   :effect: During your Draw Phase: If you control fewer than 2 Hearts,
    draw 1 card.
   :rulings: This is a passive bonus that is especially helpful at the 
    beginning of the game. This ability does not take effect until your 
    second turn.

.. ability::
   :name: Combiner
   :classification: A
   :effect: Twice per turn: Discard 2 Clubs: Draw 3 cards; Your last club
    is treated as the total value of the discarded Clubs.
   :rulings: This ability can be useful to get extra cards and play cards
    with a higher value. It is powerful as it allows you to increase your
    last club. Using this ability starts the Club Phase. Ex. You discard
    a 7 and a 2 of Clubs. You draw 3 cards and may play 1 card with a 
    value of 9 or less.

?

.. ability::
   :name: Deadly
   :classification: P
   :effect: When you destroy an opponent's Heart: The opponent discards a
    random card.
   :rulings: This ability allows you to add a little extra sting to your 
    attacks. To discard a card, pick a card from the opponent's hand.

?

.. ability::
   :name: Direct Hitter
   :classification: P
   :effect: Flip: Until the end of your turn: Your Shield Bypass attack
    power is 25% plus 25% for each Diamond the defender controls.
   :rulings: It may seem like your bypassing becomes a little weaker, but
    it still has a minimun of 50% attack power when it matters. 
    Theoretically, you could do 125% damage if you attack a player with
    Landowner.

? Double Player
  
? Eccentric

? Fair Trade

.. ability::
   :name: Fisher
   :classification: A
   :effect: Once per turn: Pay 4 points: Target one player and reveal one
    card in your hand; The targeted player must give you a card from hand
    with the revealed card's value if able; Otherwise, draw 1 card; If its
    value is equal to the value of the revealed card, both of those cards
    have a cost of 0 until the end of your turn.
   :rulings: This is a complex, but effective ability with a benefit in
    all cases. It allows you to steal cards from your opponents and 
    coordinate with teammates when Ally is insufficient. The cost effect
    only applies to Utility Cards. If the targeted player has more than
    1 card with the designated value, it is that player's choice which
    card to give.

precedence? blessed

.. ability::
   :name: Fulfilled
   :classification: P
   :effect: During your Draw Phase: If you hold 5 or more cards, do not 
    draw; Otherwise, draw until you hold 5 cards.
   :rulings: A very good ability that is especially helpful in the 
    beginning of the game. This ability does not take effect until the
    start of your second turn.

.. ability::
   :name: Gambler
   :classification: A
   :effect: Twice per turn: Discard the top card of the deck; If the deck
    card his a lower value than the card from your hand, draw 2 cards.
   :rulings: This ability encourages you to discard high value cards, so
    you have a greater chance of being able to draw. Keep in mind that as
    the game progresses, fewer high value cards are in the deck. You do
    not draw on a tie. Ex. You discard a 6 and the deck card is a 4. You
    draw 2 cards.

.. ability::
   :name: Grave Robber
   :classification: A
   :effect: Once per turn: Target one card in the discard pile; Pay points
    equal to that card's value: Add that card to your hand.
   :rulings: This ability may be costly, but it allows you to choose a card
    from potentially many options. Prepare for future turns with this 
    power, and control which cards are available.

.. ability::
   :name: Haggler
   :classification: P
   :effect: The costs of Utility Cards you hold are reduced by 1.
   :rulings: In some situations, this is even better than being able to 
    play more points. Aces are free.

.. ability::
   :name: Healthy
   :classification: P
   :effect: The value of the Heart with the lowest base value that you
    control is doubled.
   :rulings: This is the only ability that gives you a health boost. 
    Sometimes it is better to have one high heart than multiple lesser
    hearts. Ex. You have an 8 and a 5 of hearts, so you have 
    8 + (5 * 2) = 18 health.

.. ability::
   :name: Hopeful
   :classification: A
   :effect: Pay 4 points: Draw 1 card; If it is a Heart, you may 
    immediately play it for free.
   :rulings: This is a very good ability that allows you to draw more cards
    and can be used if you ever need more Health.

?

.. ability::
   :name: Illusionist
   :classification: A
   :effect: Target 1 card controlled by any player; Pay points equal to
    that card's value: Return that card to its controller's hand.
   :rulings: This is a versatile ability as it allows you to disable
    opponent defenses, reduce opponent attack power, and upgrade your 
    own board. You may not use this ability on a card whose controller
    has a full hand.

.. ability::
   :name: Impenetrable:
   :classification: P
   :effect: You may not attack or be attacked until round 4. While you have
    a full board, you may not be attacked. At the start of your turn: If
    you have a full board, destroy 1 card on your board.
   :rulings: This ability is useful to get through the early rounds. You
    may still play Spades starting round 3. It also gives special protection
    at a self-destructive cost. This ability may help you survive, but you
    may need to sacrifice protection to attack.

.. ability::
   :name: Indebted
   :classification: A
   :effect: Once per turn: Pay 4 points: Play a Utility Card for free; You
    may not play any more cards this turn.
   :rulings: This ability is useful when you have several cards you can play
    in a turn, but are short a few points, and lacking Clubs.

.. ability::
   :name: Innovator
   :classification: P
   :effect: Diamonds you control may be used to attack; Their attack power
    is cut in half.
   :rulings: This is an ability that is not too powerful, but can be useful
    for delivering a final blow. Take care not to leave yourself defenseless
    Always round down. Round after you add together the values of the
    Diamonds. Ex. You attack with a 5 and 4 of Diamonds. (5 + 4) / 2 = 4.5
    which rounds down to 4 attack power.
    
.. ability::
   :name: Investor
   :classification: P
   :effect: At the start of your Point Phase: Gain 2 points for each 
    Diamond and Spade you control.
   :rulings: This card seems like a good ability with a potential 24 
    points in one turn. Unfortunately, you won't have any space to use
    all those points.

.. ability::
   :name: Landowner
   :classification: P
   :effect: You may have up to 4 cards of the same suit on the board.
   :rulings: This is a powerful ability, but only if you survive long 
    enough to use it. Potentially, you could have 12 cards on the board
    at once.

.. ability::
   :name: Large Capacity
   :classification: P
   :effect: Your full hand is 16 cards. During your Draw Phase: Draw 1
    card for every 4 cards in your hand.
   :rulings: This ability is useful in some situations. It gives you a 
    bonus to help you grow your hand. It is effective in a long game.
    Beware of the player who gets this ability with Loaded.

? Life Feeder

.. ability::
   :name: Lifeline
   :classification: P
   :effect: While you only control 1 Heart, your Shields cannot be bypassed.
   :rulings: This card is ideal to help you get through the first few 
    rounds. However, it may become useless if you lack Diamonds or a 
    strong Heart card.

.. ability::
   :name: Limiter
   :classification: A
   :effect: Pay 4 points: Target an opponent: Declare a suit; If the 
    targeted opponent holds a card of that suit, that opponent must discard
    a card of choice.
   :rulings: This is a highly strategic ability. It allows you to target
    certain cards that you do not want your opponents to have. If you 
    notice that an opponent does not discard a card of the declared suit,
    you can call the same suit again to increase the punishment.

.. ability::
   :name: Loaded
   :classification: A
   :effect: Pay 12 points: Draw until you have a full hand; You may not
    play any more cards this turn.
   :rulings: This ability is very useful to open possibilities on the next
    turn. Its obvious downside is its cost. 

? Loophole

.. ability::
   :name: Manipulator
   :classification: A
   :effect: Once per turn: Pay 3 points: Draw 1 card; Place a card from 
    your hand on the top of the deck.
   :rulings: This is a decent ability that can be used to annoy your 
    opponent, and it is good for the long game. It is a bit cumbersome
    as you often do not want to draw back the card you placed on the deck.

.. ability::
   :name: Maximizer
   :classification: A
   :effect: Pay 3 points: Return a card you control to your hand a play a
    different card of the same suit for free that costs up to 3 point more.
   :rulings: This ability is useful in the long game when you have a solid
    defense with a full board. You may play a card with a lower value than
    the one you returned to your hand. The card played must be physically
    different, not necessarily nonequivalent. Ex: You return a 6 of Hearts
    to your hand; you may now play up to a 9 of Hearts.

.. ability::
   :name: Neutralizer
   :classification: A
   :effect: Destroy one Diamond you control: Destroy a Spade controlled by
    an opponent with a base value less than or equal to the base value of 
    the destroyed Diamond.
   :rulings: This is a powerful ability as it enables you to reduce 
    opponent attack power and prevent shield bypasses. The obvious risk
    is leaving yourself defenseless.

.. ability::
   :name: Options
   :classification: A
   :effect: Skip your Draw Phase: Gain 6 points at the start of your
    Point Phase.
   :rulings: It may not be necessary often, but this ability can be 
    effective as it increases your standard number of points by 50%. You
    choose to either draw or play cards. You may not use this ability until
    the second turn.

.. ability::
   :name: Pacifist
   :classification: A
   :effect: Thrice per turn: Discard a Spade: Draw one card.
   :rulings: This ability is good in the early game as it allows for a
    one-to-one trade when Spades are unplayable. It is less useful in 
    the later game when attacking is more demanding.

.. ability::
   :name: Plagued
   :classification: A
   :effect: Once per turn: Pay 4 points: Discard 1 card: All cards on a 
    board with a base value equal to the discarded card's base value are
    destroyed.
   :rulings: This can be a good card, but it is tricky to use as it 
    affects all players. It is best when used with a Club.

?

.. ability::
   :name: Purifier
   :classification: A
   :effect: Discard all the cards in your hand: Draw 1 card or each 
    discarded; You may shuffle the discard pile into the deck.
   :rulings: This ability allows you to completely refresh your hand if you
    have nothing you want. It also allows you to shuffle the discard pile
    into the deck which may be beneficial.

.. ability::
   :name: Recycler
   :classification: A
   :effect: Once per turn: When you play a Club: Discard 1 card: You may
    play a card from the discard pile instead of a card from hand. 
   :rulings: This is a powerful ability as you can play high-valued cards 
    straight from the discard pile.

.. ability::
   :name: Replenished
   :classification: A
   :effect: Once per turn: If you have 0 cards in you hand, draw 2 cards.
   :rulings: This may not be needed too often, but it is a solid ability
    to keep your options open. This is a mandatory effect that can activate
    in the middle of another effect's resolution.

.. ability::
   :name: Resilient
   :classification: P
   :effect: When you lose a Heart: If you survive, you may immediately play
    a Heart for free.
   :rulings: This ability is very good and will make opponents think twice
    before attacking you.

.. ability::
   :name: Resourceful
   :classification: P
   :effect: The values of your Clubs are increased by 2.
   :rulings: This is a good card that can help you play higher valued cards.
    With this ability, the lowest value of a Club that you can play is 3.
    Remember that the number of cards drawn from a Club is determined by
    its Base Value.

? Scavenger

.. ability::
   :name: Seer
   :classification: P
   :effect: During your turn, you may look at the top card of the deck.
   :rulings: This ability allows you to see what you would get if you drew
    a card. It is a good way to maximize the effect of a Club.

? Seizure

.. ability::
   :name: Seller
   :classification: A
   :effect: Discard up to 3 Utility Cards: Gain points equal to half the 
    cards' total value; Draw 1 card for every 2 discarded.
   :rulings: When you have cards you do not need, this ability is effective.
    It is versatile in that it can be used for points or new cards. 
    Remember to round down when the points are calculated.

.. ability::
   :name: Sorcerer
   :classification: A
   :effect: Once per turn: Target a Spade you control; Pay point equal to
    its Base Value: Until the end of your turn, its value is doubled, and
    you may only attack with that Spade.
   :rulings: This ability allows you to boost your attack power for a hard
    hit. It is best when you are lacking other Spades.

.. ability::
   :name: Standardization
   :classification: P
   :effect: All Clubs you play allow you to draw 2 cards.
   :rulings: This is a very good ability for increasing your drawing power.
    Hopefully you have some 6-10 of Clubs.

.. ability::
   :name: Toughness
   :classification: P
   :effect: The values of Diamonds you control are increased by 1.
   :rulings: This ability gives you a little extra defense that can be the
    difference between a damaging blow and a final blow.

.. ability::
   :name: Trade Master
   :classification: A
   :effect: Once per turn: Discard 1 card: Draw 2 cards: Discard 1 card.
   :rulings: This ability is an upgrade on the Trader ability. You only need
    to discard 1 card to start, and you may discard one of the cards you
    drew afterwards.

.. ability::
   :name: Warrior
   :classification: P
   :effect: The values of Spades you control are increased by 1.
   :rulings: This ability adds a little extra punch to your attacks, and it
    doubles the power of your Aces.

.. ability::
   :name: Wealth
   :classification: P
   :effect: You start each Point Phase with 15 points.
   :rulings: This ability has no downsides apart from the fact that you 
    might not take full advantage of it. When played with other point 
    bonuses, apply this one first.

.. ability::
   :name: Wisdom
   :classification: A
   :effect: Once per turn: Pick up the top 3 cards of the deck and look at
    them; Put them back in any order.
   :rulings: This ability allows you to choos what you will draw, and what
    players after you will draw. If there are fewer than 3 cards in the 
    deck, pick up as many cards as possible. The discard pile is not
    shuffled into the deck. While a player is looking at the cards, they
    are still considered to be in the deck.

.. _stack_abilities:

Stack Abilities
***************

This section covers abilities that are only relevant when playing with the
Stack. See :doc:`/stack`. When using these special abilities, mix them in with the
others.

Coming Soon.
