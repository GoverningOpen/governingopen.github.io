Title: An Introduction to Governance
Challenge: fear-of-governance
Authors: Shauna Gordon-McKeon
Summary: What is governance, and why should you care about it?

### What is governance?

Governance is a fancy (scary, sometimes maligned) term for “collective decision-making”. If you work with one or more other people, and you make decisions, then your project has governance. Surprise!

Most people think governance means “who’s in charge”, and governance definitely encompasses that. But it also includes many other kinds of decision-making, such as picking what goes in releases, creating roadmaps, designing APIs, encouraging community members to take on responsibility, dealing with code of conduct violations, budgeting, and more.

Many people also think that governance means “long, boring processes that take forever”. Unfortunately, a lot of governance is like this. Horrible bureaucracy is a fairly common failure mode. But not all governance is slow and process-heavy. For example, [do-ocracy](https://www.noisebridge.net/wiki/Do-ocracy) has little to no written rules, but it's still a form of governance. It's just informal and implicit. This style of governance works for some and not for others (it’s got some [failure modes](https://www.jofreeman.com/joreen/tyranny.htm) too). If you’re concerned that governance will slow your project down, check out our tips for [avoiding bureaucracy](https://governingopen.com/resources/avoiding-bureaucracy).

Finally, some people are looking for the “right way” to do governance. Unfortunately there is no one right way, any more than there’s one right way to build a website. All we’ve got are best practices. Governance is very context-dependent. Things like project size and age, the kinds of users a project has, the funding situation, the history of a project and its existing culture, organizational or corporate involvement - all these factors and more may influence a project’s governance. 

### Governance as infrastructure investment

Governance is a kind of infrastructure, like a test suite. Think about it: 

Writing tests for code can be a lot of effort, but you do it because you know it will save you time and aggravation later. Similarly, governance can be more work in the short run, while saving you lots of time and emotional energy in the long run.

Another similarity is how, when you’re writing tests, you can't just copy and paste from another project’s tests into your own. You can get templates, but you have to adapt the test to fit your project’s specific needs. Governance is also context sensitive. You can copy processes from other projects, but you have to adapt them, too.

If your code changes, the tests that are covering them sometimes have to change. Similarly, governance should change if the project changes. If you go from being all-volunteer to getting a million dollar grant, for instance, you probably want to adjust how financial decisions get made.

Tests become more and more vital as a project grows. You might get away with not having a test suite when your project is small, but as your project impacts more and more people, you’ll want the reliability that tests can help give. Similarly, as the project grows, you're going to need better governance. But you can probably get away with not thinking about it when it's just you and a couple friends. 

Finally, governance processes are like test suites because some bugs are always going to slip through. You can do your best and catch a lot of problems with tests, but you're never going to catch 100%. Similarly, even the best governance processes don’t prevent all governance problems. You’ll still need to work through issues occasionally. You can use these moments as opportunities to check if your governance processes are still working for you.

I really like this metaphor, although it’s not perfect. For one thing, we’re not really aiming for 100% governance process coverage. That would be too much governance. We also don’t need to have governance processes happening by default. Many people run tests multiple times a day as part of CI systems. But you probably only want to trigger a governance process when you need it. Finally, while tests are always explicit and formal, governance can be explicit and formal but it can also be implicit and informal. Culture and personal relationships are a huge part of governance that shouldn’t be overlooked.

### Three levels of governance

One framework I have found immensely helpful in thinking about governance is Elinor Ostrom’s three levels of governance. Ostrom was a nobel-prizing winning economist who studied [how communities manage common goods](https://www.actu-environnement.com/media/pdf/ostrom_1990.pdf), and many people have applied her work to open source software and other “intellectual commons”. Ostrom divided governance into three layers: the operational, collective, and constitutional layers. 

The collective level is the one most people think of when they hear the word “governance”. Who is in charge, and how do they make decisions? Answers might be, “we've got a BDFL (Benevolent Dictator For Life), and they make all the decisions” or “the core team decides by consensus, and then the steering council votes when the consensus can't be reached.”

The operational level of governance is the day-to-day. Who has merge rights and are they actually using them? Who owns the server, who moderates the mailing list, and how is that going? Who do people in the community actually trust? Whose weekend gets ruined when something breaks?

Finally, there's a constitutional level of governance, which answers the question “who decides who decides”. If the collective level describes who is in power and the power they have, the constitutional level is the meta-level above that. 

My favorite example of a constitutional transition in open source is the 2018 Python governance transition. I gave [a whole talk](https://www.youtube.com/watch?v=mAC83JVDzL8) about it! The TLDR is: in 2018, Guido Van Rossum stepped down as the BDFL of Python after nearly 30 years. He didn’t say “this is my replacement” or “this is what you should do now”. He said, “I trust the core developers to figure it out”. And so the core developers had to figure out what came next. They didn’t just have to decide who would replace Guido. They had to decide how to decide. 

| Governance Level | Question Answered | Frequency | Example: US Government | Example: Python Language | 
| ----------- | ----------- | ----------- | ----------- | ----------- | 
| Operational | What is the decision? | day to day | parking tickets, jury duty | individual PEP decisions, release management, CoC enforcement |
| Collective  |  Who makes the decisions? | recurring (ie quarterly or yearly) | elections, rules of the House & Senate | steering council elections |
| Constitutional | Who decides who decides? | very rarely | constitutional convention | core maintainer deliberations codified in [PEP 8000](https://peps.python.org/pep-8000/) |

Open source communities should be interfacing with these three levels differently. 

For the operational level, the goal should be to *monitor* and make sure you’re getting feedback about problems. You shouldn’t be thinking about governance every day, but you want to make sure you have some mechanisms in place that will help you notice patterns.

At the collective level, the goal is to *maintain* your processes: to document them, carry them out correctly, and update them when they’re not working. 

At the constitutional level, the goal is to *be prepared*. I recommend setting up a default answer (a [constitutional backstop](https://governingopen.com/resources/who-decides-who-decides)) for how you’ll decide what your new governance structure will be if you ever need to change it. That way you can focus on figuring out the best governance structure for your project, and not on the meta-question of how you’re going to decide that.

### Next Steps

Hopefully I’ve convinced you that governance is at least worth thinking about. If you’d like to learn more about governance and how it works in open source, you can browse this site and its resources. 

We also offer [free consultations](https://cal.com/shauna-gordon-mckeon/governance-consult), [virtual and in-person workshops](https://governingopen.com/get-help.html), and a [Matrix channel](https://matrix.to/#/!vMlUdIiTlurpzHadvV:matrix.org?via=matrix.org) for folks to ask questions.

If you have any feedback on the site, or want to contribute yourself, check out our [Github repository](https://github.com/GoverningOpen/governingopen.github.io/)!

