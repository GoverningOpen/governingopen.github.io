Title: Build a Constitutional Backstop
Authors: Shauna Gordon-McKeon
Challenge: transitioning-governance
Summary: Answering the question "Who decides who decides?" can help prevent a governance crisis.



When we think of governance, we often think about existing systems for decision-making. Most children in the United States are taught about the three branches of government, and how elections work. Or contributors to a project might know that so-and-so is the BDFL who gets to decide what changes get incorporated into the project.

That *is* governance, but it's only one kind of governance. According to [Elinor Ostrom](https://en.wikipedia.org/wiki/Elinor_Ostrom), there are three levels of governance in a given community: the operational level, the constitutional level, and the collective choice level.

The operational level consists of the specific decisions being made on a day to day basis. A maintainer merging a pull request, a mayor approving a budget, or a farmer taking only the water they need from a shared well are all forms of operational governance. It answers the question **"what is the decision?"**

The collective choice level consists of the specific rules and roles in place which direct those decisions. The rules for how someone becomes a maintainer, the elections process for the mayor, or the carefully deliberated on rules for irrigiating crops are part of the collective level. It answers the question, **"who makes the decisions?"**

The constitutional choice level sits behind all of that. It determines how the rules of the collective level get put in place. It answers the question, **"who decides who decides?"**

| Governance Level | Question Answered | Frequency | Example: US Government | Example: Python Language | 
| ----------- | ----------- | ----------- | ----------- | ----------- | 
| Operational | What is the decision? | day to day | parking tickets, jury duty | individual PEP decisions, release management, CoC enforcement |
| Collective  |  Who makes the decisions? | recurring (ie quarterly or yearly) | elections, rules of the House & Senate | steering council elections |
| Constitutional | Who decides who decides? | very rarely | constitutional convention | core maintainer deliberations codified in [PEP 8000](https://peps.python.org/pep-8000/) |

In the Python language project, decisions are made through the [PEP process](https://peps.python.org/pep-0001/) as well as through the deliberations of the steering council which oversees (and is elected by) the core maintainers. On any given day, a given PEP might be approved or a decision handed down by the steering council. Lower stakes decisions are also made on a regular basis by everyday maintainers. This is the operational level of governance. The PEP process itself, and the rules by which the steering council is elected, is the collective level of governance. When changes need to bemade to the collective level of governance - for instance, in 2018/2019 when Guido van Rossum stepped down, and the steering council was created - that is constitutional governance.

You may have noticed that constitutional questions come up quite rarely. It is tempting to ignore this level of governance entirely. Many open source projects start off with a sole maintainer who evolves naturally into the project's BDFL. The BDFL typically thinks of themselves as the one who makes all the decisions. But they are also, implicitly, the answer to the question, "Who decides who decides?"

Sometimes, when projects are ready to transition away from a BDFL model, they get stuck on the question, "Who decides who decides?" They don't want the answer to be "the BDFL" - the whole point of the transition is often to make the project more democratic. Or maybe they just don't feel like any of the options is "legitimate".

("Legitimacy" is actually a very fuzzy concept when it comes to the constitutional level of governance. When the US Constituion was created, many people decried it as illegitimate because delegates to the 1787 constitutional convention had only been authorized to amend the Articles of Confederation, not replace them. For more on the fuzziness of legitimacy, try Arthur Applbaum's ["All Foundings Are Forced"](https://www.hks.harvard.edu/publications/all-foundings-are-forced). tl;dr whatever most people feel is legitimate is legitimate.)

You can make your project's eventual transition easier by working out the constitutional level of decision-making ahead of time. You can say, "when we transition governance, the process will involve X and Y stakeholders." Doing so is not a firm commitment - the current leadership can alter this document at anytime - but it provides a default process that can hopefully make your eventual transition quicker and easier.

Sketching out the constitutional layer of governance can also highlight barriers to transition. For instance, if there are no stakeholders to involve at the constitutional level, that's a sign that you need to work on relationship-building and community-building before you can transition. Or if you're worried that two stakeholder groups will be at odds with each other, perhaps the community needs to address that conflict separately from figuring out a new governance structure.

It's important not to let this decision grow stale. If you say "our council of advisors will pick the new governance model when the time comes" and then the council of advisors ceases to exist, that's not great. Review it regularly like you would any other documentation. Hopefully, when the time comes, you'll be glad you were prepared.


(Note: This article has a lot of overlap with my PyCon 2019 talk ["A New Era in Python Governance"](https://www.youtube.com/watch?v=mAC83JVDzL8). If you like videos, you might enjoy watching!)