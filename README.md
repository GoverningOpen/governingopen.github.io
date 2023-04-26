# The Governance of Open Source

This repository contains materials (guides, exercises, etc) for open source projects looking to tackle various governance challenges. We believe that by learning about how past projects have tackled problems, we can avoid unnecessary stress and cultivate happier, more functional communities.

The repository also contains a bare bones static site generator to display these materials via github pages.

The repository is structured around **Governance Challenges** which are specific challenges that recur across many different projects. These include, but are not limited to:

* Figuring out what kind of governance you have
* Making decisions about what tasks to work on
* Deciding on and establishing community norms
* Raising and/or distributing money
* Cultivating new leaders from among the community

Some of these challenges may not seem like pure "governance challenges", but we believe that governance plays a vital role in how these situations develop and thus how they need to be addressed.

For each challenge identified, we seek to collect exercises, tools, wisdom and anecdata that can help future projects tackle these challenges. As we develop this knowledge base, we hope to identify which approaches are most helpful in a given context so we can make recommendations with more confidence. In the end, though, there is never "one right way" to address a governance problem. All we can do is make our best guess.

# Ways to Contribute

## Suggest new challenges and resources

We use our issue tracker to discuss [new challenges](https://github.com/shaunagm/Open-Source-Governance-Workshop/labels/new%20challenge). Anyone is welcome to suggest a challenge, but please check for duplicates first. Please select the [new challenge issue template](https://github.com/shaunagm/Open-Source-Governance-Workshop/tree/main/.github/ISSUE_TEMPLATE) when prompted.

Each challenge has resources associated with it. These are exercises, tools, stories, etc that projects can learn from. You can suggest new resources (or flesh out existing ones) by leaving a comment on the associated challenge.

## Add new challenges or resources on the site

Once a challenge or resource has been developed enough, it can be added to the site through a pull request. The steps are broadly the same for challenges and resources.

To add a new challenge/resource, go to the corresponding subdirectory under the top level `content` directory. Copy an existing file and remove the existing metadata values and content. You can then add your own.

A few notes:

* All metadata must go at the top of the file with no blank lines between them.
* Metadata keys are not case-sensitive.
* Authors are primary creators of the page for a challenge or resource, so if you're adding one you're an author. If you're making a minor edit to a file you'd add yourself as a contributor.
* Resources have an extra metadata field, "Challenge". This allow us to display associated resources on the challenge page.

If you're up for it, feel free to build the site and check that the file looks the way you want, but I will also be double-checking when reviewing PRs so you can skip that step if you want.

## Organize a workshop

The Open Source Governance Workshop series is being piloted at PyCon US 2023, and there has been interest in having it at other events. If you would like to bring the workshop series to a meetup or conference, please reach out. We are also happy to work with individual projects.

## Fund this work

This workshop series is being funded by a small carve out from an NSF grant. If you are interested in funding further development of this work, please reach out.