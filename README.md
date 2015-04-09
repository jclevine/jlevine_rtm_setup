# Setup RTM for jlevine's "system"

You may have seen [my RTM Forum post](https://www.rememberthemilk.com/forums/tips/18744/) about my beloved system.

It looks pretty intimidating at first, but if you use this script to setup, literally 50% of those instructions are unnecessary.

Below is a copy of the instructions (excluding the ones you no longer need after using this script):

# jlevine's RTM System

## WHAT ADDING MY TASKS LOOK LIKE
So, what's my system? First let's define which fields I populate and what I populate them with.

Example Quick Add:

    Write RTM system into RTM forum. !1 @internet #iu #f1 #e1 #anytime [optional ^in 1 week 19:00] =1 hr

Let's break this down:

### Priority - Example: `!1`
Straightforward: In whatever quadrant it lies, how important is this task? This one happens to be very important!

### Context/Location - Example: `@internet`
The ever-famous context. Here's a list of the ones I use. I find that everyone has their own and really any would work in this system.
1. anywhere - Anywhere. Duh.
2. home - Something I can only do at home (like laundry or talking with my spouse about something).
3. internet - Doesn't matter where I get access, I just need the internet.
4. out - Out and about. Usually shopping/errandy things.
5. phone - I probably don't really need this context, but I like to differentiate between internet and phone since I prefer a landline for phone calls.
6. waiting <-- Very important and very useful later.
7. work - Something to do at work (although I keep 2 accounts -- 1 for work and 1 personal -- I keep "work" tasks in my personal account when referring to life things like using a scanner at work for something "personal" like emailing a picture to a friend since I don't have a scanner).

But wait! We're just through the contexts! :D

#### **WARNING!**
The RTM API doesn't allow creation of locations/contexts yet so you'll have to create all of these manually -- do that before running the script!

### Tags - Examples: `#iu, #f1, #e1, #anytime`
This particular task is a Quadrant-1 (**i**mportant **u**rgent task), it's very **f**un (1 out of 3), it will take great amounts of **e**nergy (1 out of 3 range), and I can do this "any time" during the day or night.

I think this is generally straightforward except I will give the possible tags for a couple of them:

1. Quadrant Tags - I add a couple extra non-7-Habits quadrants since I like to differentiate between important (bills, emergencies) and "somewhat" important, which I definitely want to do, but my life won't collapse if I don't get to it.

    `iu, inu, siu, sinu, niu, ninu.`

2. Time Window - When can I do this?

    `anytime, morning, work, lunch, afternoon, evening`

### Due Date - Example: `^in 1 week 19:00`
When things must definitely happen at a specific time. This works particularly well when you have it notify you when things are due via your phone. This field is also very important for @waiting contexts. But again, we'll hear about that soon enough. Use this field sparingly, I think.

### Estimate - Example: `1 hr`
Just nice for when you want to do some fun searches. Say you want an easy task that's fun, and you can do within an hour? Simple:
    `tag:f1 AND tag:e3 AND timeEstimate:"< 1 hr"`

## IN DEFENSE OF MY SMART ADD REQUIREMENTS
But even putting in each task might seem like a lot! You have to put in all those fields and remember each one! I have 4 retorts/comments:

1. At first you keep a little cheat sheet to remind (no pun intended) you each time you add a task to put in all the appropriate fields. Just a little piece of paper or txt file that says something like this:

    `[task] !_ @context #iu/inu/siu/sinu/niu/ninu #f_ #e_ #[time of day] ^[optionally due] =_ minutes/hours`

2. I suggest you add the tags in the same order every time you add a task. That way it becomes easy to make sure you got all of them, which leads to...

3. After literally about a week or 2, it becomes so rote that it just flows out the fingers without any thinking. It takes me maybe 5 - 10 seconds to put in one task.

4. I steal an idea from a [really-complex-system guy](https://www.rememberthemilk.com/forums/tips/8327/) and make an "Error" Smart List, so you know quickly if one of your tasks is missing something vital.

## WORKFLOW

So you wake up and the first thing you always do, because you're a go-getter, is to load up ol' RTM. What do you do when it loads up?

Simple! Start from 0_* and slowly make your way down to 6_error. The highest priority things tend to show up in 0, 1, 2. Once those fires are put out, you can move on down the line.

That's it! Go have fun and never worry about missing anything ever again! Below is an example of what I think upon opening RTM if you, like me, learn by example. Thanks for reading this exceedingly long post! You're a real trooper.

## EXAMPLE: THIS IS WHAT I DO WHEN I WAKE UP AND OPEN UP RTM.

1. `0_due_soon`

  Hrm. There are a few things that are overdue. I really should do those. I'll be sure to do them later today.
  Eek. That really important thing is due tomorrow!
  That errand that I wanted to do in 2 days is there. Good to know.

2. `1_urgent_important`

  Oh man, that really important thing is due tomorrow! Now that I've seen that twice, I'll be sure to get off my ass and do it!

3. `2_urgent`
  Here is a list of about a dozen tasks that are urgent (including AGAIN the really important task from `0_due_soon`) or are pretty important and urgent, but not life and death things.

4. `3_important`
  If you're a diehard 7-Habits Guru, this is your bread and butter. Not necessarily urgent things, but they're really important to you. And yes, again, the really important task due tomorrow shows up. See the pattern here?

5. `4_somewhat_important`
  Same as `3_important`, but a little less important. This is where the majority of my tasks are (I have 199 tasks of my total 266 tasks sitting in here). It is really important to have this category's tasks appropriately prioritized. Try to only keep a few Priority-1 things that really **are** pretty important things, and maybe even bordering on actually important over somewhat_important, but not quite.

  If this list is really unwieldy, you might even use a fancy, little-known search option "`addedBefore`". So if you search for:

    `list:somewhat_important AND addedBefore:"2014-04-08"`

  you'll get some tasks that you made quite some time ago, so maybe you should do something about that.

6. `5_error`
  Look in here just to be sure none of your tasks are not showing up in one of the lists above. Don't want one of them hiding.

## I ALMOST TOTALLY FORGOT TO EXPLAIN WAITING
Oops. Luckily, it's simple:

If, say, you just emailed Bob the Monkey and you want to follow up in a week if he doesn't respond (monkeys are often forgetful). I would add the following task:

    Waiting to follow-up with Bob. !2 @waiting #inu #f1 #e2 #anytime ^in 1 week 19:00 =25 min https://mail.google.com/mail/u/2/#inbox/24a47b3f94186557

It is very important to have a due date when you're waiting, otherwise it will never show up when the day you're waiting for finally arrives! And when I'm waiting on a response, I like to put a link to my email. If you're using Outlook, you can just put the Subject line in your Notes so you can search for it later.
