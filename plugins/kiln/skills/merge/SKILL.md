---
name: merge
description: Finish a piece of work - merge the branch into the integration branch (develop), push, delete the branch (and its worktree). No CI here - it only runs when a release goes out (/kiln:release).
argument-hint: "[branch]"
---

Branch: `$ARGUMENTS`, otherwise the current branch. Integration branch: the one the project's
`CLAUDE.md` names, otherwise `develop` if it exists, otherwise `origin`'s default branch.

The merge happens here, directly: no pull request nor approval to wait for ([NO-COMMIT-ON-MAIN]).
A pull request already open for the branch turns "Merged" on GitHub by itself at the push of
step 4. Talk to the user in their language.

1. On the branch: everything is committed (`git status --porcelain` empty), otherwise stop and
   say so. Then review the branch (`/kiln:review <branch>`): after the push of step 4, its
   commits are public for good. What the review tidies on the branch happens before the merge;
   what it leaves to the user, tell them and wait for their decision.
2. Update the integration branch (`git pull --ff-only origin <integration>`), then
   `git merge --no-ff <branch> -m "Merge branch '<branch>' into <integration>"`, from the main
   tree when it is on the integration branch, otherwise with `git -C` on a worktree that is;
   never switch the branch of the main tree under another session.
3. On a conflict: stop, show the conflicting files, propose a resolution.
4. `git push origin <integration>`.
5. Delete the worktree and the branches right away: a merged branch is not kept aside. Only if
   the merge really is in `origin/<integration>`:
   - `git fetch -q origin`, then `git merge-base --is-ancestor <branch> origin/<integration>`
     succeeds: every commit of the branch, so each of its files, is in the published
     integration branch;
   - the worktree is clean (`git -C <wt> status --porcelain` empty).
   Then `git worktree remove .claude/worktrees/<name>` (never `--force`), `git branch -d
   <branch>` (never `-D`) and, if it exists on GitHub (`git ls-remote --heads origin <branch>`),
   `git push origin --delete <branch>`. If a check fails: delete nothing, say which one and why.
6. No CI after the merge: `kiln ci` only runs when a release goes into `main` (`/kiln:release`),
   the only state that is deployed. In a repo without a production `main` (the integration branch
   deploys itself), GitHub's CI follows the push. Typing ran before the push (pre-push hook): if it
   fails, fix it on the branch.
7. Sum up: merge commit, files touched.
