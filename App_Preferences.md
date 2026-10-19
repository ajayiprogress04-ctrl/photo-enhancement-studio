# My App Design Preferences

Version 19 · Consolidated from the Meiosis and Chromosome 9 app discussions · Updated 18 October 2026

## How to use this brief

Read this before designing or modifying one of my apps. Treat it as my default preference, while following any newer project-specific instruction. Inspect the existing target project and the latest accessible reference source. Implement the work and deliver the complete project; do not stop at recommendations. Ask only for essential missing information. Work systematically and continue through the agreed steps without asking me to say “next” after each one.

Short request for a future app:

> Use My App Design Preferences. Inspect my existing project and the latest Appendicitis Hub source, preserve the features I need, and build a visually simple app in that design family. Show short content first, keep details expandable, and deliver all changes in one complete ZIP.

This brief is portable. It does not guarantee that every unrelated future chat automatically receives it. Attach or select it in a new chat, or include it among the project reference files/instructions.

## 1. The design standard

Reference app: https://appendicitis-learning-hub.vercel.app/
Reference repository: https://github.com/ajayiprogress04-ctrl/appendicitis-learning-hub

Use the reference as a design and interaction standard. Inspect actual HTML, CSS, JavaScript, assets, configuration and recent commits when accessible. Do not assume the deployed site contains every repository update. Never modify the reference when working on a different target app.

Reuse its real design patterns where practical: Source Sans 3 interface typography, Cormorant Garamond headings, ruby/burgundy actions, navy, bronze and green accents, subtle scientific linework, compact panels, restrained gradients and familiar navigation. Adapt imagery and content to the new subject. Do not import clinical variables, statistical workflows or unrelated research functions into an educational app.

Prefer recognisable continuity over a generic template. Avoid oversized headings, excessive white space, thick decorative borders, busy dashboards and rows of competing buttons.

## 2. Colours and readability

I prefer much deeper, richer colours with strong contrast in ALL three themes: Light, Dark and Colour. Improving only the Colour theme is insufficient. Use visibly richer backgrounds, surfaces and action colours in each theme; a small accent-only change does not satisfy a request for deeper colours. Keep text bright on dark surfaces and very dark on light surfaces.

- Light: very dark, clear text against readable lighter surfaces, with deep burgundy, navy, bronze and green accents.
- Dark: near-black backgrounds with bright, readable text and visible control boundaries.
- Colour: deep burgundy/plum and other rich panels, with bright text that remains easy to read.
- Use colour deliberately; do not make text faint, washed out or low contrast.
- Keep secondary text, inputs, links, selected states and focus indicators readable too. Check contrast rather than simply darkening everything.
- Decorative backgrounds must stay subtle and must not interfere with text or scientific figures.

## 3. Show less at once

My default is visually simple, compact and uncluttered. Do not display long paragraphs, every objective, every explanation or every tool at once.

Show short summaries, then reveal extra information through clear expandable sections, dropdowns or focused views. Preserve all important educational content behind those controls; do not omit it just to shorten the screen.

For the Meiosis app, I specifically removed:

- The landing Continue your learning panel, completion progress bar and Continue learning button; Quick guide remains.
- The wide All objectives / Objective 1–8 button row; use a dropdown.
- The intermediate objective lesson-card listing; selecting an objective opens its first lesson directly.
- The right-hand lesson panel containing Your Progress, Mark complete, Bookmark lesson and In This Objective.
- The repeated Original slide wording & source disclosure on each lesson; original documents remain available in Original Slides.
- The six-button lesson toolbar: Quick revision, Expand sections, Collapse sections, Look up selected text, Help and Copy lesson link.

These are established simplification choices for Meiosis. For another app, do not automatically introduce similar clutter. Retain a control only when it serves the new app's actual task or I request it. Do not re-add removed controls merely because they once existed.

## 4. Navigation and learning sequence

- Use the familiar ☰ three-line button to collapse and expand the desktop left panel; remember the choice. On phones, use it to open the navigation drawer.
- Categorise objectives under expandable class/module headings, rather than one long flat list. Meiosis uses Class 1 and Class 2.
- Use a compact objective dropdown on the landing page and inside lessons. Group options by class and identify the current objective. The primary design must be objective based: numbered learning objectives govern navigation and lesson sequences. A topic list alone is insufficient. Label objectives inferred from source material as learning objectives rather than inventing author-stated research objectives.
- Choosing an objective opens its current saved example and immediate practice question.
- Show multiple lessons one after another, one lesson at a time, with Previous/Next and an indicator such as Lesson 1 of 2.
- Clicking Next or Previous opens the destination at the TOP, even if previously visited.
- Returning from a glossary explanation or diagram is different: restore the precise lesson/visual, scroll position, focus and reading context.
- Make the destination and return actions obvious. Avoid redundant navigation panels.
- Every question-review or practice sequence needs a clear End review action at the bottom. It returns to the overview at the top without resetting answers or saved work.

## 5. My glossary and explanation rules

Golden rule: Explain the WHY in seconds.

Use direct, simple, clear, concise and memorable language. Avoid textbook paragraphs, unnecessary introductions, vague definitions and repetitive wording.

Show one concrete example first, with its demonstrated answer, a short explanation and immediate practice. Plain meaning and scientific definitions support that example; keep longer definitions and mechanisms in optional reference details.

Make additional details available separately:

- Why this name? Give the naming logic or origin only when known and supported.
- Why does it work this way? Explain the mechanism simply.
- Remember it this way: a short memory aid.
- A worked example and a separate practice question are required for every glossary term. Keep the initial view short and reveal the teaching sequence progressively.
- Related terms and relevant source/lesson links.

Underline and link every relevant scientific term, abbreviation and methodological phrase throughout readable learning content, not only a separate Useful terms list. Cover inflections and full forms with context-appropriate glossary entries. Use visible underlining, preserve readable text and avoid nested links, form fields, navigation controls and misleading common-word matches. Keep quiz answer options intact. Original raster labels must remain unchanged; provide a linked explanatory key below the image instead of pretending text inside an image is interactive. Make important terms, abbreviations and appropriate diagram labels clickable. Keep search convenient. Do not display every full definition while browsing term names. Explain uncertain or unavailable information honestly; do not manufacture definitions, etymologies or image interpretations.

Provide both previous-term navigation and an explicit return to the originating lesson/diagram. Back must restore the previous position, not reopen a different page at the top. Preserve the underlying reading content where possible.

## 6. Diagrams and document previews

Pictures should be visually simple and educationally accurate. Preserve supplied scientific figures and original meaning.

Numbered diagram markers must correspond to the correct features and stay aligned when resized. Never reuse arbitrary fixed marker positions across unrelated diagrams. If a location has not been established, use a labelled numbered key below the image instead of implying a verified spatial annotation.

After opening a label explanation, Back to diagram restores the same visual, scroll position and focused label. Back to Lesson then restores the lesson.

PowerPoint and Word previews should follow the focused document-viewing approach in the reference Hub: a large readable document, minimal surrounding text, clear page/slide navigation, zoom, fit width, download and full screen where supported. Extra extracted text and thumbnails should not dominate the screen.

A PowerPoint image preview is not proof of a Word renderer. Implement and test the document types actually needed; do not claim unsupported types work.

## 7. Guide, developer identity and sharing

- Keep Quick guide easy to find on the landing page.
- Keep three explicit actions together on the landing page: Quick guide, Share app and Copy link. Copy link must be visible, not hidden only as a Share fallback. It copies the clean production app address without opening the native sharing menu. Prefer native sharing for Share app, with clipboard and visible-link fallbacks.
- Provide a clearly labelled User Guide and About the Developer, without dumping lengthy text on screen.
- Use my actual approved developer biography, qualifications and portrait from the current reference or supplied profile. Do not replace it with a generic “creates useful tools” description or infer identity from unrelated account history.
- The reference currently identifies Progress Ajayi. Recheck the current published profile before copying changing qualifications or status.
- Use the supplied app logo in appropriate branding and social-sharing metadata. Link sharing must include a dedicated raster PNG/JPEG preview containing the app icon/title, plus crawler-readable Open Graph metadata and appropriate card tags. Generate absolute image and canonical addresses at build/server time from the real production URL; do not rely on runtime JavaScript or a favicon alone. Keep PNG favicon/touch-icon variants. Test after deployment where possible, and account for access protection, cropping and cached previews without claiming universal display.
- Share a clean, professional public production address, rather than a long preview/deployment address. Never invent domain availability or claim a domain was configured when it was not.
- Sharing previews are controlled partly by each platform; do not guarantee universal logo display without testing.

## 8. Engineering, source accuracy and delivery

Inspect and improve the actual existing project. Keep the target app separate from reference projects. Preserve valid recent changes and useful working functionality.

For PowerPoint learning apps, inspect the supplied source documents first. Preserve important text, figures, tables, questions and source references. Organise by actual learning objectives; clearly label objectives inferred from headings or content.

Use maintainable content files, local assets where practical and minimal dependencies. Avoid paid services and API keys for the core experience unless agreed. Support mobile and desktop, usable controls, keyboard focus, readable text and helpful error states. Preserve existing user data through compatible updates.

Test relevant workflows and build the actual project. Separate automated logic/simulated-DOM checks from real-browser, responsive, full-screen and sharing verification. Never claim to have tested, committed, pushed or deployed something without evidence.

Deliver ONE complete project ZIP containing all updates so far, not a patch that depends on earlier downloads. Include brief beginner-friendly instructions for running locally, uploading the extracted contents to the intended GitHub repository and deploying to Vercel. Provide concise change notes, significant files, test results and remaining issues. Do not make me repeat prior preferences or assemble multiple versions.

Keep messages concise. Explain the result and the next essential action. Ask focused questions only when genuinely needed.

## 9. Consolidated corrections to carry forward

| My correction or request | Rule for future work |
|---|---|
| Colours need to be much deeper in each theme | Make substantial, visible palette improvements in Light, Dark and Colour, including backgrounds, surfaces and actions. Preserve contrast; do not change only one theme or only accent colours. |
| Every necessary word should be underlined and linked | Provide visible inline glossary links for relevant scientific concepts, terminology, abbreviations and methodological phrases throughout readable educational content. A separate list of useful terms alone is insufficient. |
| The app should be objective based | Organise the main experience by numbered learning objectives, grouped into expandable classes/modules. Use objective dropdowns on Overview and inside lessons, open the saved current example directly, and identify the current objective and step number. Apply objective-based filtering to practice and revision where relevant. |
| The app icon should appear when sharing its link | Supply a dedicated preview image containing the app icon/title and static sharing metadata tied to the actual production address. Prepare and test the implementation; be honest about untested live previews and platform limitations. |
| I need help from naming through deployment | Give practical, beginner-friendly steps for naming, extracting/running the app, creating the intended GitHub repository, uploading the correct folder contents, deploying to Vercel and checking the actual production address. Do not assume an unfinished step is complete. |
| I need the preference file to keep | Provide the latest consolidated preferences as a standalone downloadable Markdown file when requested, not only inside the project ZIP. Preserve earlier requirements unless explicitly superseded. |

## 10. Current Chromosome 9 app decisions

These are specific to **Chromosome 9 Study Desk**, not compulsory counts or structures for every future app:

- Repository/app identifier: `chromosome9-study-desk`; subtitle: “Understand the evidence. Explain the study.” No production domain has been confirmed in this discussion.
- Six inferred learning objectives govern 15 lessons across two expandable classes: study foundations/methods, then results/interpretation/defence. These are educational objectives derived from the manuscript, not six invented author-stated research objectives.
- Latest implementation: 105 glossary entries, 56 existing flashcards and 30 questions. New terminology must not silently change existing question/card identifiers or reset saved work.
- The manuscript is a secondary descriptive sequencing-data analysis, not a review article or a patient cohort. Preserve that distinction in lessons, questions and presentation practice.
- Keep the manuscript as the scientific authority; use oral slides for rehearsal, the poster for concise communication, and this brief for design. Record disagreements rather than merging them silently.
- Preserve the deeper Light palette with warm tan surfaces and dark wine/navy/green text, true-black Dark surfaces, and deep-plum/burgundy Colour surfaces. These describe the latest implemented direction; browser visual acceptance is not assumed from automated contrast tests.
- Preserve the chromosome icon across app branding, browser/touch icons and the sharing card. The latest sharing card is a 1200 × 630 PNG; its production image address is configured during deployment.
- Keep progress and notes browser-local with backup export/import, and preserve the existing storage key through compatible updates. Do not promise cross-device synchronization.
- The project contains research documents. Use a private repository by default and explain that a private repository does not itself make the deployed site private. Do not remove access protections merely to force a sharing preview.
- Deliver the complete cumulative project ZIP. Keep the current preference brief inside it, while also providing this standalone file when requested.

## Updating this brief

For every complaint, correction or preference I express about my apps, update this brief as part of that task without waiting for me to ask again. Record the reusable rule, amend the relevant section, and resolve the older conflicting rule. Do not treat an app-specific request as a universal rule unless that is clearly intended. Keep general defaults separate from decisions specific to one app. Preserve this document as the reusable source of truth, and include the latest copy with future project handovers.

### Revision notes

- Version 6, 18 October 2026: consolidated all retained requirements and corrections; added a correction-to-rule summary, beginner deployment guidance, standalone Markdown delivery and clearly separated current Chromosome 9 project decisions.

- Version 5, 18 October 2026: sharing the app link should show its icon/title through dedicated social-preview artwork and static metadata, with real production URLs and deployment verification.

- Version 4, 17 October 2026: confirmed substantially deeper palettes in all three themes, inline underlined glossary links throughout learning text, and numbered objective-based navigation with lessons grouped beneath objectives.

- Version 3, 17 October 2026: added an End review action after practice questions, returning to the overview without clearing answers.

- Version 2, 17 October 2026: added an explicit Copy link beside Quick guide and Share app; made updating this brief after every complaint/correction an ongoing instruction.
- Naming decision: retain Meiosis Learning Hub; the proposed broader rename was declined.

## Teaching beyond the supplied literature

Do not limit teaching to what the manuscript explicitly defines. Explain established scientific concepts with verified authoritative sources, including clear meaning, mechanism, why it matters, and worked examples. Explain names when their expansion or naming logic is known; omit empty naming sections instead of repeating “not defined in the literature.” Explain relevant gene functions with appropriate uncertainty.

Clearly separate established background, this study’s reported findings, and interpretation or uncertainty. Link background explanations to their sources. Never invent missing study methods, measurements, validation, clinical implications, or historical naming stories. Use the literature to anchor the research, while helping learners understand the underlying science.

Chromosome 9 update: version 1.3 adds sourced background explanations and gene functions, worked examples, and optional meaningful naming sections. Study limitations remain explicit.

### Glossary coverage of titles and phrases

Include important phrases from the app title as well as individual scientific terms. Explain ambiguous wording in context: “public acute leukemia” refers to publicly available acute leukemia sequencing datasets; “public” does not define a disease subtype. Support searchable aliases and underlined links in explanatory prose, and connect phrase entries to their component concepts.

## Show diagrams and tables where I learn

Display relevant methodology diagrams, result figures and tables directly within their corresponding objective lessons, with clear captions, source references and brief interpretations. Do not rely only on a separate visual-library link or downloads. Keep a visible gallery with actual previews and an obvious overview entry point. Preserve original figures; label newly created teaching schematics. Support readable responsive images and horizontally scrollable tables, and retain enlargement controls.

### Returning from a visual

“Back to visual library” and browser Back from a figure or table must restore the previous gallery scroll position, not restart at the top. Reserve image dimensions so late-loading previews do not shift the restored view. Keep intentional Previous/Next lesson navigation starting at the top.

## Explain every diagram like the lesson text

Each methodology diagram and result figure needs a short explanation of what it shows, how to read its labels/axes/colours/symbols/arrows, a walkthrough, why it matters to the objective, and a memorable takeaway. Include interpretation limits and source references. Explain tables by their rows, columns and units. Underline and link important scientific terms in these explanations to the glossary. Keep the initial explanation short and further teaching expandable, both inside lessons and in enlarged visual views. Deliver all agreed updates together in one complete project ZIP for uploading at once.

## Connect every visual to its objective

Make objective connections explicit and clickable. Group methodology, figures and tables by learning objective in the visual gallery. Every lesson should offer its objective’s visual evidence with a brief explanation of each connection; individual visuals must link back to their objective. Allow a visual to support multiple objectives where appropriate, without inventing author-stated research objectives. For synthesis/limitations objectives, link the relevant existing evidence and explain when no separate original figure exists.

## Flexible return from visual evidence

Use a context-aware Back button for figures, tables and methodology views. Return immediately to the actual previous view, including the exact objective lesson, gallery or previous visual, and restore scroll position and expanded reading sections. Do not force every return into the visual library. Keep the visual library as a separate navigation option and provide a safe fallback for directly opened visuals. Normal Previous/Next lesson navigation should still start at the top.

## Permanent Learning Design Standard: Objectives, Worked Examples, Independent Practice, and Feedback

### Scope and governing principle

Apply this standard to every appropriate future application that teaches, explains, trains, revises or assesses knowledge, and to upgrades of existing educational applications. It is a foundational default, not a temporary request for one project. Do not force exercises into unrelated non-educational workflows.

Use this sequence: **Learning objective → One informational example and demonstrated answer → Immediate practice question → My answer → Brief feedback → Next example → End-of-objective transfer check.** Teach reasoning that the learner can immediately apply in a different situation. Reading, opening a page and revealing an answer do not prove mastery.

### Observable objectives and connected activities

Every major module, topic, lesson and meaningful subtopic needs a clear outcome appropriate to its scope. Use observable verbs such as define, identify, explain, interpret, compare, differentiate, calculate, apply, predict, analyse, evaluate, construct or justify. Avoid “learn about” when a specific outcome can be stated. For example: “Interpret a p-value and distinguish statistical significance from effect size and practical importance.”

Connect each outcome to its explanation, worked demonstration, independent question, feedback and assessment. Keep learning objectives derived from sources distinct from research objectives actually stated by an author. Scientific diagrams, tables and glossary subtopics must identify the objective they support.

### Required worked-example structure

Every concept taught must have an appropriate example. Use a familiar situation first when helpful, then the subject-specific setting. Include all of the following:

1. A concrete scenario or problem.
2. The concept or principle being demonstrated.
3. The relevant information.
4. Step-by-step reasoning.
5. The correct answer or outcome.
6. Why the answer is correct.
7. A short transferable principle to remember.

For quantitative work, give the formula, substitution, calculation, units and interpretation where applicable. For mechanisms, identify components and the order or relationship of events. For conceptual work, demonstrate classification, comparison or evidence interpretation. For literature appraisal, demonstrate comparing explanations or identifying a limitation. Do not force arithmetic into a non-numerical concept.

Clearly identify hypothetical teaching scenarios and invented example numbers as hypothetical. Distinguish them from reported study findings. Never invent patient histories, published findings, citations, measurements or missing methods and present them as real evidence. Explain a genuine evidence gap instead of filling it with fiction.

### Required independent practice and answer control

Immediately after the demonstration and its answer, offer a separate “Your turn” question testing the same principle with changed numbers, context, biological material or evidence. The task must require a fresh application, not repeat the demonstration verbatim or ask the learner to copy its answer.

Show the current example and its one practice question together. Keep future steps hidden until the learner responds. Keep the practice answer and feedback hidden until a submitted attempt. Give a hint before the solution when the learner struggles. An optional hint should guide reasoning without giving the complete solution. Use suitable controls: choices, numerical entry, free text, ordering or diagram tasks according to the skill and implemented capabilities. Do not imply unsupported interaction types exist.

For a numerical task, accept a meaningful tolerance and units where supported. For free text, use a transparent rubric and allow scientifically valid wording. Do not claim automated language grading when the learner is comparing their own response with a model.

### Explanatory feedback, further practice and transfer

After a submitted attempt, show the correct answer, reasoning steps, why the answer follows, how the demonstration’s principle transfers, common mistakes and a brief takeaway. For an incorrect response, explain the likely misconception where the selected option supports that inference. Do not present a red cross as sufficient teaching.

For open responses, distinguish correct reasoning, partially correct reasoning and remaining gaps through a rubric. Accept valid alternative explanations. Allow the learner to mark their response accurate, partial or needing revision, and label that as self-assessment. Do not infer accuracy from exact wording alone.

Offer another distinct opportunity after difficulty. A transfer or mastery check should change the setting or add a relevant complication. Keep quiz scores, independent attempts, assisted reveals and self-assessed performance distinct. Record useful progress without presenting it as validated mastery, clinical readiness or competence.

### Every glossary entry is a small learning activity

A definition alone is insufficient. Every entry must include an example with its demonstrated answer and reasoning, a different practice question, and answer/feedback after the appropriate action. Also include the term, abbreviation expansion where applicable, simple meaning, scientific or technical explanation, relevance, common confusion, related concepts and source reference.

Use “not applicable” for fields that genuinely do not apply, such as an acronym expansion for an ordinary word. Do not invent an expansion, etymology or historical naming story. A conceptual, scientific, classification or interpretation scenario is suitable when an everyday or numerical scenario would be misleading.

### Apply the method throughout educational features

Use the same principle across objectives, lessons and subtopics, concept clusters, scientific mechanisms, statistical/computational tutorials, question banks, revision, case-based work, visual interpretation, comparisons, methodology, oral rehearsal and practice assessments. Adapt the presentation to the skill, rather than forcing identical wording everywhere.

For a figure or table, demonstrate interpreting one part and ask the learner to interpret a different part or changed hypothetical example. For oral rehearsal, provide a model explanation and then a comparable audience question. Flashcards can connect to worked demonstrations and application practice; recall ratings remain self-assessments.

### Implementation, persistence and validation

Inspect the actual project before designing the implementation. Reuse its technology stack, data conventions, colours, typography, responsive layout, navigation and existing state. Add reusable content structures and teaching components. Keep the brief explanation visible and longer examples expandable, with minimal clutter.

Validate that required objectives, scenarios, information, reasoning, answers, principles, practice, feedback, rubrics and sources exist. Placeholder text such as “example coming soon” is invalid. Validate objective references and activity links. Make lesson completeness a content-quality requirement, not a claim of learner mastery.

Preserve saved notes, answers, schedules and preferences. Add compatible progress fields or migrate old backups safely. Preserve answer history or attempt counts, distinguish answer reveals from independent submissions, and do not erase previous work when providing another exercise.

Test the actual paths: start practice, enter/select an answer, submit, receive feedback, request a hint, explicitly reveal, self-assess a free response, try another scenario, attempt a transfer check, refresh, export/import and return to the same reading context. Test hidden-answer behaviour and escaping of learner text. Verify coverage of every glossary term and relevant learning surface. Separate real browser/mobile checks from simulated-DOM and static checks, reporting unperformed checks honestly.

### Reuse and delivery

For a future educational app: read this brief, identify learning features, map objectives to demonstrations and practice, use subject-appropriate scenarios, provide feedback and further practice, validate completeness, test and preserve the remaining preferences. Request missing essential files; reuse available current source files instead of requesting redundant uploads.

Update this existing preference file in place and preserve its identity and unrelated requirements. Provide the updated standalone Markdown and one complete cumulative project ZIP, with implementation notes, actual test results, missing examples or unsupported features and remaining work. The portable file must be attached or selected in a future context; saving it does not guarantee automatic access by every future conversation.

### Chromosome 9 implementation record

Version 2.0 adds a structured teaching activity for each glossary entry, lesson and source-visual interpretation, with related applications for comparisons and oral rehearsal. Keep hypothetical practice separate from manuscript findings. Local learning records must distinguish independent multiple-choice scores, explicit reveals and rubric-based self-assessments. The existing question bank, flashcards, objective navigation and flexible visual return remain available.

## Example-first guided learning and dropdown selections

This section refines the permanent learning standard above. It governs future appropriate apps and upgrades of educational apps.

My main teaching experience must be: **one useful informational example → one related question → my answer → feedback → the next example**. Restructure unsuitable existing flows to follow it; do not merely add another optional learning card to long notes.

- Break objectives into small steps. Show only the current example, demonstrated answer, concise principle and one comparable question. Use a changed scenario or numbers so the learner applies the principle.
- Place the example before the definition in the glossary. Keep technical definitions, naming, scientific detail and sources as optional reference after the example/application. Do not open a term with several paragraphs to memorise.
- Explain correct answers briefly. For a mistake, explain the misconception or calculation issue without pretending to know more than the response reveals, offer a hint and another opportunity, and keep longer reasoning expandable.
- Make Continue available after a response and feedback. Do not automatically jump forward before the learner can respond. Free-text work uses an explicit rubric and self-assessment. Remember the current step and reviewed steps, allow revisiting, and give a short transfer check at the end of each objective. Process completion and self-assessment are not validated mastery.
- Apply the pattern to relevant lessons, glossary, calculations, visual interpretation, comparisons, rehearsal, revision and question banks. Navigation and original reference material do not require exercises. Retain essential scientific evidence and limitations, reorganised into small teaching steps or accessible reference rather than deleted.
- Keep selection controls as dropdowns wherever appropriate. I like this compact selection style. Use it for objectives, reviewed-step selection, terminology, comparisons, answer choices, filters, recall ratings, self-assessment and evidence selection. Replace unnecessary button rows, tabs or long simultaneous option lists when a dropdown serves the task clearly. Keep direct actions such as Submit, Try Again and Continue as clearly labelled buttons.
- When upgrading another app, audit its selection groups and apply the same dropdown convention where suitable. Do not claim to have changed an unavailable app or force dropdowns onto unrelated direct actions.
- Verify example-before-question order, answer gating, response-specific feedback, retry, Continue, end checks, saved-step restoration, safe backup import, reference access and glossary/visual return. State browser/mobile verification limits honestly.

Chromosome 9 version 2.1 introduces saved guided objective paths, example-first term dialogs, one comparison at a time and dropdown selection for the remaining bank choices and ratings. It preserves original source documents, essential facts, scientific uncertainty and prior saved learning records.

## Repeated practical learning in objectives and glossary — 18 October 2026

Keep the screenshot-approved layout: One example → Demonstrated answer → Why → Remember → expandable worked reasoning → Your turn. Use this in both objectives and glossary entries.

Give every concept several distinct practice opportunities, not just one question or a definition. In this app, expose three sequential tasks: apply the concept, correct a mistaken claim, and transfer the reasoning to another situation. Make correction and transfer part of the normal journey rather than optional hidden extras. Keep questions practical and relevant to the specific concept; use calculations where suitable and distinguish hypothetical exercises from actual study findings. Do not count reworded duplicates as new scientific evidence.

Show one question at a time, immediate feedback after an attempt, a visible task count and saved position. Require a response and feedback review for all three tasks before the normal Continue action leaves the concept. Written explanations use an explicit rubric and honest self-assessment, not claimed automatic understanding or certified mastery. Allow revisiting reviewed tasks through a dropdown; preserve independent glossary navigation and the flexible Return button. Existing responses, notes, objectives, visual evidence and themes must remain usable. Record activity completion separately from correctness.

Current implementation: app 2.2.0, all 105 glossary entries and each ordinary guided objective concept use the three-task sequence. Existing sourced exercises are promoted into the main flow; no new manuscript results are invented. Two end checks per objective remain available. This standard applies when modifying future accessible apps; unrelated apps have not been modified here.

## Example-first app as the default experience — 18 October 2026

Worked examples are the main way I understand and remember concepts. Make them the central learning experience throughout my app, with many practical cases across the objectives and glossary, figures and tables, comparisons, revision and presentation practice. Preserve the approved visual structure: One example, Demonstrated answer, Why, Remember, optional worked reasoning, then Your turn and feedback. Prefer this to long explanatory pages or dense dashboards.

Simplify navigation and reduce competing content. Use a short dropdown of main learning destinations and place supporting tools, lengthy notes and references in expandable sections. The current main destinations are Start/continue, Learn an objective, Worked examples, Practise a term, and Figures and tables. Make the start page immediately useful with the saved concept and its worked example. Keep search, dropdown selections, flexible return, themes, sharing and backups.

Increase the number and variety of worked cases, not just the number of menu items or repetitions of the same question. Include practical interpretation, calculations with clearly hypothetical values, correction of misconceptions, and transfer questions. Do not invent manuscript results. Label related topic cases distinctly from an example about the precise glossary term. Preserve scientific qualifications and access to source evidence even when reducing visible content. Progress should resume at the saved task, and shared activities should stay consistent when returning from the glossary.

Current app 2.3.0 adds 30 authored hypothetical worked cases and 90 follow-up tasks across all 15 topics. The library now exposes 175 worked-example units with three tasks each (525 authored tasks, some reused across app surfaces). All glossary entries offer their own term example and two related topic cases. This replaces the previous crowded main menu with five main destinations; supporting tools remain available under More practice and reference. This preference should guide future accessible app updates; unrelated apps were not changed here.

## Simplify practice; examples teach first — latest correction, 18 October 2026

My latest preference supersedes the earlier mandatory three-stage practice and rubric requirements. I learn better from practical worked examples than from many definitions or meanings. Let examples do most of the teaching. Give a short why with feedback and keep definitions as optional brief reference only.

Remove the screenshot-identified learning clutter: the worked-reasoning disclosure, the Practice 2 of 3/reviewed-task panel, written peer-review exercises, long model-answer and transferable-rule sections, rubric checkboxes, self-assessment dropdown and save button, and the Common confusion and sources panel within the practice card. Do not replace these with another compulsory assessment process.

Use the simple pattern I prefer: One example → Demonstrated answer → Why → Remember → Your turn (dropdown choice) → brief feedback → Another question or next example. One answered question is enough to continue; the other questions are optional practice. Do not require me to type an explanation, check rubric points or finish three tasks to move on. Keep objective navigation, saved position, glossary links and original evidence available. Preserve old private answers and notes in backups even when their old interfaces are removed.

Current app 2.4.0 retains 175 worked-example units and offers three dropdown questions per unit, available one at a time without a three-task gate. Old question-bank and flashcard URLs now open the simple example library. Glossary definitions remain optional; sources and scientific qualifications remain accessible outside the uncluttered practice card. This is my app design preference, not a claim that definitions are unnecessary for every learner or subject.

## Numerous examples with systematic study coverage — 18 October 2026

Build a large, organised collection of practical worked examples that helps me cover the particular study’s concepts, methods, findings, evidence interpretation and applications. Quantity alone is insufficient: audit coverage against the actual research objectives, methodology, results, figures, tables, terminology and limitations. Fill identifiable gaps with varied, relevant practice rather than superficial rewording.

For each study topic, include six aspects: understand the idea, apply it in a different situation, read the actual evidence, spot a mistaken inference, connect methods to results, and defend the study in examiner or conference questions. Progress from straightforward demonstrations to connected interpretation and defence. Include calculations where appropriate, with the correct unit and denominator. Link study-based examples to the relevant source figure, table or methodology. Distinguish reported observations, derived arithmetic, hypothetical examples and unknown information.

Keep the simple approved layout: Example → Demonstrated answer → Why → Remember → dropdown question → brief feedback → Another question or next example. Definitions stay optional and brief. Do not reintroduce written exercises, rubric checklists, self-assessment panels, compulsory three-stage completion or a crowded main menu. One answered question remains enough to continue. Optional dropdown filters may organise practice by objective or skill.

Maintain a coverage map that links topics and practice skills to concrete activities, checks all glossary and visual references, and records unresolved evidence gaps. Update it when adding new material. Never invent missing results, exact plot percentages, undocumented software behaviour or clinical evidence. Describe coverage as content availability, not proof of complete knowledge or validated mastery.

Current implementation: app 2.5.0 adds 45 worked cases across all 15 topics: evidence interpretation, method connections and study defence. The app now has 220 example activities representing 200 distinct worked scenarios and 660 dropdown-question slots. Shared concepts are reused across app surfaces. Every one of the six objectives, 15 topics, 105 glossary entries, seven result figures, two tables and the methodology visual is mapped in COVERAGE_AUDIT.md and content/coverage-audit.json. The optional practice-focus dropdown exposes the six learning aspects. Earlier notes, answers and progress are preserved; older final-check cursors enter the added practice cases before the concluding checks.
