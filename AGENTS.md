# AGENTS.md

Owner: `evento-globolo`  
Tracking: `DEN-1889`

Preserve the responsive Astro product site, product-specific event-platform copy, existing production build and test scripts, configured GitHub Pages URL, SEO metadata, and deployment behavior. Do not replace working product content with a placeholder or generic template.

Before proposing changes, run:

```bash
npm test
npm run build
python3 scripts/verify_repo.py
```

Use focused pull requests, preserve public URLs and interface compatibility, add tests with behavior changes, never commit credentials or customer data, and resolve conflicts semantically using both sides and the relevant history.

## Repository-local Git worktrees

- Create or use a Git worktree only when the human operator explicitly authorizes it for the current task. Concurrency or a dirty checkout is not permission by itself.
- Put every authorized worktree at `<repository-root>/tmp/worktrees/<name>`; from the repository root, use `./tmp/worktrees/<name>`. Never place worktrees beside repositories or organization directories.
- Keep `tmp`, `temp`, `tmp/worktrees`, and `temp/worktrees` ignored in the repository-root `.gitignore`. Do not commit files from those directories.
- Relocate or remove a worktree only when the operator explicitly requests it. Before removal, preserve and publish intended changes, verify its commit is represented on the target branch, and confirm there are no tracked, untracked, ignored-sensitive, or in-use files that must survive. Remove it with `git worktree remove <path>` without `--force`; never delete a worktree directory with `rm`.
