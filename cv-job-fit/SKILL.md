---
name: cv-job-fit
description: Optimize, tailor, format, or evaluate Hendrix Freire's CV for a specific job description. Use when the user asks to optimize the CV, adapt the CV to a vacancy, format the CV for a role, check whether the profile fits a job, compare the CV against a job posting, or improve job-match/ATS alignment. Always base the work on the file `projects/cv-hendrix/output/cv-hendrix-freire.md`, produce a compatibility index, preserve factual accuracy, and generate an updated markdown CV plus a PDF version tailored to the target role.
---

# CV Job Fit

Use this skill to adapt Hendrix Freire's CV to a specific vacancy without inventing facts.

## Core rules

- Read `references/paths.md` first.
- Treat `projects/cv-hendrix/output/cv-hendrix-freire.md` as the single source of truth.
- Never invent achievements, tools, metrics, employers, dates, education, certifications, or responsibilities.
- Rephrase, reorder, condense, and highlight only what is already supported by the source CV and the user's clarifications in the current chat.
- Mirror relevant keywords from the vacancy when they are honestly supported by the source CV.
- If the vacancy asks for something not evidenced in the CV, mark it as a gap instead of faking alignment.

## Workflow

1. Read the base CV from `projects/cv-hendrix/output/cv-hendrix-freire.md`.
2. Read the vacancy text, link, or pasted description.
3. Extract the vacancy's core signals:
   - target title and seniority
   - must-have skills
   - nice-to-have skills
   - business domain
   - leadership vs hands-on balance
   - recurring keywords and ATS phrases
4. Score compatibility from 0 to 100 using this simple frame:
   - 40 points: hard-skill overlap
   - 25 points: experience/seniority overlap
   - 20 points: domain/context overlap
   - 15 points: tooling/keyword overlap
5. Return a short diagnostic with:
   - compatibility index
   - strongest matches
   - real gaps
   - positioning advice
6. Produce a tailored CV text that:
   - keeps all facts true
   - reorders emphasis toward the vacancy
   - uses vacancy keywords where truthful
   - improves ATS readability
   - keeps the writing natural, not robotic
7. Save the tailored CV as a new markdown file in `projects/cv-hendrix/output/`.
8. Generate a PDF version of the tailored CV in the same folder.
9. Present the user with:
   - compatibility index
   - a concise rationale
   - suggested wording changes
   - paths to the new `.md` and `.pdf`

## Output standard

Always provide these sections in the response:

- `Compatibilidade: X/100`
- `Pontos fortes`
- `Lacunas reais`
- `Ajustes aplicados no CV`
- `Arquivos gerados`

## Writing guidance

- Prefer strong, concrete wording over generic corporate filler.
- Keep Portuguese natural and readable.
- Use bold sparingly for truly important wins.
- Optimize for both ATS scanning and human reading.
- If the user only asks whether the profile fits the vacancy, still compute the compatibility index and offer a tailored CV draft unless the user says not to.

## PDF rule

After generating the tailored markdown, generate a PDF version too. Reuse the existing CV project layout and renderer patterns when possible; if needed, create or adapt a renderer inside `projects/cv-hendrix/` instead of writing temporary files outside the project.
