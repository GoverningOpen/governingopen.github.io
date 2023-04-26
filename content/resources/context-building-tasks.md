Title: Context-Building Tasks
Authors: Shauna Gordon-McKeon
Contributors: Toshio Kuratomi
Challenge: cultivating-community-leadership
Summary: Tasks which allow a newer contributor with little context about the project to learn gradually while meaningfully contributing.


Many potential contributors have a desire to contribute but lack knowledge about the codebase and the community that would help them contribute effectively. **Context-Building Tasks** are tasks which do not require a lot of context, at least at the beginning, but encourage the contributor to learn more and more context as they continue with the task.

Context-building tasks often require significant mentorship/oversight at first, but over time (as context is learned) the contributor will require less help. Ideally, context-building tasks become a "net time saver" to the existing maintainers within a few weeks or months, if not right away. This initial mentorship period can also help build relationships which is important for retention.

### Triage Teams

"Issue triage" is the process of reviewing and responding to new issues in an issue tracker. It typically involves some combination of:

* reading the issue and identifying if any standard information is missing (for example, the version the reporter is using, or how high a priority the issue is for them) 
* applying appropriate labels to the issue
* mentioning/tagging members of the community who can help respond to the issue
* doing the social labor of letting the reporter know that they have been heard and their report is appreciated

Issue triage does *not* involve actually attempting to solve the issue! However some elements, like knowing who to tag in or how to label the issue, can be tricky at first due to lack of context. 

Triage teams are people who are assigned to process incoming issues. Depending on how active the project is, these teams may involve many people. For an example of a larger project that uses triage teams, see the [Python Software Language](https://devguide.python.org/triage/triage-team/).

### Pull Request Reviews

Most pull requests to a project, especially those from an outside contributor, require some kind of review. While people who are new-ish to a project cannot fully review most PRs, they can provide additional or initial reviews which address straightforward/obvious problems.

New reviewers should be encouraged to ask questions. This not only helps them learn about the project, it can sometimes be a signal that the code or documentation needs to be more readable. 

Projects which encourage PR reviews from new/outside contributors include [CircuitPython](https://learn.adafruit.com/contribute-to-circuitpython-with-git-and-github/giving-a-review), [Ansible](https://docs.ansible.com/ansible/latest/community/how_can_I_help.html#review-and-submit-pull-requests), [Fast API](https://fastapi.tiangolo.com/help-fastapi/#review-pull-requests), [Apache Beam](https://blogs.apache.org/comdev/entry/an-approach-to-community-building), and [Kubernetes](https://kubernetes.io/docs/contribute/review/reviewing-prs/).

CircuitPython has a particularly detailed and helpful [guide for new reviewers](https://learn.adafruit.com/contribute-to-circuitpython-with-git-and-github/giving-a-review).

### Release Notes and User-facing Release Summaries

Cutting a new release can require expert judgment to decide what should be included and what should not, but writing up reader-friendly release notes is something that a relatively new person can do. This can include looking up contributor information so that contributions that made it into the release can be credited appropriately. The release manager can then review the draft release notes to make sure they are correct - hopefully a much quicker process than having to draft and edit the release notes themselves.

Some projects also write up blog posts and social media summaries of major releases, including things like screenshots/demos to help users better understand any changes. Again, this is something that a newer contributor can take the lead on and which provides a great benefit to the community.

### Documenting Community Activity (Mailing lists, Meetings, etc)

 For larger, more active communities with busy chats or mailing lists, other kinds of summaries, beyond release notes, may be helpful. Longtime Python core developer and current Steering Council member Brett Cannon spent his early days in the Python community writing up mailing list summaries, which were greatly valued by the community.

 New contributors may also serve as notetaker during group meetings. Toshio Kuratomi writes about their experience doing this for a larger project: 
 
> People would meet, discuss, debate, and try to improve proposals. Being the person that took notes gave me insight into:
> 
> * What was important to the project at the moment
> * Who was working on what
> * Insight into the personalities of the people active in the project (those who attended the meetings or were making proposals)
> * An understanding of what axes people tended to fall along: pro-contributor, pro-product, concerned about process, etc.
