[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WFxExYvQ)
# 📝 Spring Term Summative

**author: Dr. [Ghita Berrada](https://www.lse.ac.uk/DSI/People/Ghita-Berrada)**

> [!NOTE]
> ## 💡 NOTES: 
>
> 1. You should only provide **code** if it adds anything to your answer: make sure your code confirms, reinforces, or complements your answers. Adding code just for the sake of it will not help you get a higher grade. 
> 2. You are free to choose the dataset(s) on which you do the analysis. **You may use one or two datasets**.
> 3. Given that the datasets can be large, you are allowed to use a subsample of the datasets. What matters is that the analysis serves as a proof-of-concept of your approach. If you choose to sample the data, simply explain how and why you did the sampling and what effect you think it might have on your results.
> 4. If you use any method not seen in the course, justify why you're using it and explain how it works.
> 5. **All analyses should be conducted in Python** using `scikit-learn`, `spaCy`, `gensim`, and related libraries where practicable.

⏲️ **Due Date**: Tuesday, April 15th, 5pm 

If you update your files on GitHub after this date without an authorised extension, you will receive a [late submission penalty](https://info.lse.ac.uk/current-students/services/assessment-and-results/exams/exam-discipline-and-academic-misconduct).

Did you have an extenuating circumstance and need an extension? Send an e-mail to 📧 [Kevin](mailto:DSI.ug@lse.ac.uk?subject=DS202W%20-%20W11+1%20Summative%20Extension)

⚖️ **Assignment Weight**:

This assignment is worth 30% of your final grade in this course.

<img src="https://img.shields.io/badge/30%25-c63c4a?style=for-the-badge&logoColor=white" alt="30%">

>[!IMPORTANT]
>## Do you know your CANDIDATE NUMBER? You will need it.
>
> _"Your candidate number is a unique five digit number that ensures that your work is marked anonymously. It is different to your student number and will change every year. **Candidate numbers can be accessed using LSE for You.**"_ 
>
> Source: [LSE](https://www.lse.ac.uk/accounting/study/New-Arrival/Exams-and-Assessments)

# 📝 Instructions

👉 Read it carefully, as some details might change from one assignment to another.

1. Go to our Slack workspace's `#ds202w_central` channel to find a GitHub Classroom link (the message announcing the summative will be pinned to the channel). Do not share this link with anyone outside this course!

2. Click on the link, sign in to GitHub and then click on the green button `Accept this assignment` (you need to accept any invitation you receive from GitHub after this within 7 days).

3. You will be redirected to a new private repository created just for you. The repository will be named `ds202w-2026-spring-term-summative--yourusername`, where `yourusername` is your GitHub username.

If you have any issues with accessing your repository, please contact us immediately on Slack (preferably) or by e-mail (you'll usually need to provide your GitHub username for us to solve the issue). Do not wait until the last minute to report an issue. You are responsible for ensuring you have access to your repository and can push changes to it before the deadline. 

1. Recall what is your LSE CANDIDATE NUMBER. You will need it in the next step. 

2. Create your own `<CANDIDATE_NUMBER>.qmd` file with your answers, replacing the text `<CANDIDATE_NUMBER>` with your actual LSE candidate number. You can use the `.qmd` file you used in previous labs as a template.

3. Then, replace whatever is between the `---` lines at the top of your newly created `.qmd` file with the following:

```yaml
---
title: "DS202W - Spring Term Summative"
author: <CANDIDATE_NUMBER>
format: html
self-contained: true
jupyter: python3
engine: jupyter
editor:
  render-on-save: true
  preview: true
---
```

Once again, replace the text `<CANDIDATE_NUMBER>` with your actual LSE CANDIDATE NUMBER.

7. Fill out the `.qmd` file with your answers. Use headers and code chunks to keep your work organised.

8. Use the `#help` channel on Slack liberally if you get stuck.

9. Once done, click on the `Render` button at the top of the `.qmd` file. This will create an `.html` file with the same name as your `.qmd` file.

    - **If you added any code,** ensure your `.qmd` code is reproducible. That is, if we were to restart VSCode and run your notebook from scratch, from top to the bottom, we would get the same results as you did.

10. Push both files (i.e `.qmd` and rendered HTML) to your GitHub repository. You can push your changes as many times as you want before the deadline. We will only grade the last version of your assignment.

11. Read the section **How to get help and collaborate with others** at the end of this document.

## "What do I submit?"

You will submit two files:

- A Quarto markdown file: `<CANDIDATE_NUMBER>.qmd`
- An HTML file render: `<CANDIDATE_NUMBER>.html`

You don't need to click to submit anything. Your assignment will be automatically submitted when you `commit` **AND** `push` your changes to GitHub.

> [!WARNING]
> ## Your HTML must be self-contained
> Your rendered HTML **must be self-contained** (i.e., all images, plots, scripts, and styles must be embedded in the HTML file).  
HTML files that are **not** self-contained will receive a penalty because they cannot be viewed offline or archived reliably.

# 🗄️ The Data

For this assignment, you have the choice between three datasets. You may use one dataset for both parts or different datasets for each part.

> [!NOTE]
> ## Reproducibility and data handling
> 
> **Do not upload your dataset(s) to GitHub Classroom.**  
> Large data files should not be tracked in version control and may cause issues with your repository.
>
> Instead, you must provide **clear reproducibility instructions** in your `.qmd` file(s), explaining:
>
> - **where** the data *would* be placed in the repository (e.g., `data/my_dataset.csv`),  
> - **how** the file would be named,  
> - **how** your code would load it,  
> - and any **additional steps** needed to reproduce your analysis.
>
> These instructions must appear in **both Part A and Part B** wherever relevant.  
> They ensure your work is fully reproducible **without** committing the dataset itself.

## Dataset 1: Glassdoor Job Reviews

[![Download CSV](https://img.shields.io/badge/Download-data-960018?style=for-the-badge&logo=download)](glassdoor_data.zip)

 You can also download this data [here](https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews)

This dataset contains approximately 840,000 employee reviews from the Glassdoor platform. Each review includes separate free-text fields for "Pros" and "Cons" of working at a company, along with an overall rating and sub-ratings for factors such as work-life balance, career opportunities, and senior management.

The dataset also includes metadata such as the company name, job title, location, and whether the reviewer is a current or former employee. Reviews span major employers across multiple industries.

*🔍 Technical note: The "Pros" and "Cons" fields are your primary text data. They represent two distinct perspectives on the same workplace, which opens up natural comparative analyses. Some reviews may be very short or formulaic.*

**Further information**: [Kaggle](https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews)


## Dataset 2: UK Parliamentary E-Petitions

[![Download CSV](https://img.shields.io/badge/Download-data-960018?style=for-the-badge&logo=download)](uk_petitions_final.csv)

This dataset contains petitions submitted to the UK Government and Parliament via the official [e-petitions platform](https://petition.parliament.uk/). Each petition includes the petition title, a longer description explaining the petitioner's argument, the current status (open, closed, rejected), and the number of signatures.

For petitions that reached 10,000 signatures, a government response is included. For petitions that reached 100,000 signatures, a record of whether the petition was debated in Parliament is also available. The dataset covers petitions from the current parliamentary session.

*🔍 Technical note: The dataset offers two distinct text layers, the petitioner's argument and the government's response, which differ markedly in register and purpose. Rejected petitions include a reason for rejection, which is also interesting text. Not all petitions have government responses.*

**Further information**: [UK Parliament Petitions Committee](https://www.parliament.uk/get-involved/sign-a-petition/e-petitions/)


## Dataset 3: Chicago Food Inspections

[![Download CSV](https://img.shields.io/badge/Download-data-960018?style=for-the-badge&logo=download)](Food_Inspections_Chicago.zip)

You can also download the data [here](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/data_preview)

This dataset contains records of food establishment inspections carried out by the Chicago Department of Public Health's Food Protection Program. The data spans from January 2010 to the present and covers restaurants, grocery stores, bakeries, school and hospital kitchens, daycare facilities, and other food-related establishments.

Each inspection record includes a free-text Violations field containing the violation codes and, crucially, **inspector comments** describing what was found on site. The dataset also includes the inspection result (Pass, Pass with Conditions, Fail), the facility type, the risk level (1–3), the inspection type (routine, complaint, re-inspection, licence), and location data.

*🔍 Technical note: The Violations field is your primary text data. It combines structured violation codes with unstructured inspector narratives. You will likely need to parse and separate these components. Some records have no violations listed (indicating a clean pass).*

**Further information**: [Chicago Food Safety Programme](https://www.chicago.gov/city/en/depts/cdph/provdrs/food_safety.html) | [Data Portal documentation](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data)


# 📋 Your Task

> [!WARNING]
> ## 🎯 Important: Quality over quantity
>
> **Do not try every method you know.** Choose your methods thoughtfully and go deep with analysis and interpretation. We value:
> 
> - **Focused analysis** with well-justified choices over scattered attempts at multiple methods
> - **Depth of insight** over breadth of techniques
> - **Decisive methodology** with clear reasoning
> - **Concise writing** (say what you need to say and stop)
>
> A submission using 2–3 well-chosen methods with deep analysis will score higher than one trying 6–7 methods superficially. Overly long submissions that repeat themselves or pad with unnecessary text will not receive higher marks: they will receive lower ones.

## Part A: Similarity and Anomalies (40 marks)

**Scenario**: You are a data analyst working for a research organization studying your chosen dataset. Your manager has asked you to provide insights into both the typical patterns and exceptional cases in the data. They want to understand: what's normal, what's unusual, and why both perspectives matter. Your manager will use your findings to brief senior stakeholders, so clarity and insight matter.

**Your task**: Using your chosen dataset, investigate both typical and atypical documents by:

1. Identifying documents that are **similar** to each other
2. Identifying documents that are **anomalous** or unusual  
3. Comparing what these two perspectives reveal about your data

Your analysis should use appropriate text mining methods and **two techniques: one for assessing similarity and one for detecting anomalies**. Explain what you discover from each approach and what the comparison teaches us about the social world.

> [!IMPORTANT]
> ## What you need to decide
>
> - What does "similarity" mean in the context of your dataset? How will you measure it?
> - What makes a document "anomalous" in your data? How will you identify unusual cases?
> - Why are these definitions and methods appropriate for your specific dataset and analysis goals?
>
> These are analytical decisions you must make and justify.

## Part B: Research Question (60 marks)

**Scenario**: Your research organization is preparing a report on your chosen dataset for relevant stakeholders (e.g., policymakers, business leaders, advocacy organizations, or other decision-makers appropriate to your data). You've been asked to investigate a specific question using data-driven methods and present findings that will inform their understanding or decisions.

**Your task**: Formulate and investigate a research question using unsupervised learning methods. Your question should be distinct from the similarity/anomaly analysis in Part A.

Your response must address:

- **Your research question**: What are you investigating and why does it matter to your stakeholders?
- **Your approach**: Which methods did you use and why? How do they address your question?
- **Your findings**: What did you discover and what does it mean in context? Provide concrete examples from your data.
- **Limitations**: What are the limitations of your approach? What assumptions did you make? What cautions should stakeholders have when interpreting your findings?
- **Ethical considerations**: Are there any ethical issues with your data or methods? How might your findings be misused or misinterpreted? Who might benefit or be harmed?
- **Why unsupervised learning?**: Explain clearly why unsupervised learning is appropriate for your research question and dataset. Why was supervised learning *not* used here? Is supervised learning feasible for the question you're trying to answer? If supervised learning is not feasible, explain why; if it is, explain why unsupervised is still the better choice.


**Note:** Your Part B analysis should use different primary methods from Part A (e.g., clustering, topic modeling, dimensionality reduction rather than similarity/anomaly detection). However, you may build on Part A findings if it makes sense for your research question. For example, you might use Part A's anomaly findings to motivate your Part B question, or use similarity patterns from Part A as one input to a broader analysis in Part B. **Well-justified connections between parts will be rewarded, not penalized.**

> [!TIP]
> ## Guidance on methods
>
> You need at least TWO unsupervised learning techniques (e.g., topic modeling + clustering, or clustering + anomaly detection).
>
> **Note**: Dimensionality reduction (PCA, UMAP, etc.) doesn't count as one of your two required techniques. It's a preprocessing/visualization step. So "PCA + k-means" counts as ONE technique (clustering). You'd need to add another method (e.g., PCA + k-means + topic modeling, or PCA + k-means + DBSCAN).
>
> **Choose methods that work together** to answer your question. Don't just apply multiple methods independently. Show how they complement each other in your analysis. Focus on **integration and insight** over trying many techniques.

> [!NOTE]
> ## What we're assessing
>
> **Part A** assesses: Your ability to work with similarity measures and anomaly detection, integrate multiple methods, compare different analytical perspectives, and communicate insights clearly.
>
> **Part B** assesses: Your ability to formulate research questions, select appropriate methods, interpret findings with concrete examples, and think critically about limitations and ethics.
>
> **Across both parts**: We value **focused, decisive analysis** over trying every method. Choose your methods thoughtfully, justify your choices, tie them to your narrative and dataset, and provide concrete examples from your findings. Quality and insight matter more than quantity.

# ✔️ How we will grade your work

A 70% or above score is considered a distinction in the typical LSE expectation. This means that you can expect to score around 70% if you provide adequate responses to both parts, in line with the learning outcomes of the course and the instructions provided.

Only if you go above and beyond what is asked of you _in a meaningful way_ will you get a higher score. Simply adding more code or text will not help. You need to provide unique insights or analyses that make us go, "_wow, that's a great idea! I hadn't thought of that_".

Here is a detailed rubric of how we will grade your answers. Note that the rigor of our marking varies with the expected difficulty of the question.

## Part A: Similarity and Anomalies (40 marks)

- **>29 marks:** Your response, besides being accurate, well-explained, effectively formatted, and surprisingly concise, surprised us positively. You might have devised a custom similarity measure logically justified for your chosen dataset, or used sophisticated anomaly detection methods with clear rationale. Most importantly, your **comparison** of what similarity vs. anomaly perspectives reveal is insightful and non-obvious. You provided concrete examples from your data (e.g., specific documents or groups) showing exactly what makes them similar or anomalous and what this reveals about social dynamics. Your code (when provided) is well-documented and your plots are excellent. You tied everything together into a coherent narrative about typical and exceptional patterns in your dataset.

- **29 marks:** Your response is well-structured and covers all requirements concisely. You applied appropriate similarity and anomaly detection methods with good justification specific to your dataset (not generic). Your **comparison** clearly explains what each perspective reveals and how they complement each other. You provided concrete examples from your data to illustrate your findings. Your interpretation focuses on what the patterns mean for your specific dataset, not generic observations. Code (when provided) is well-documented. Markdown formatting is excellent.

- **23–28 marks:** Your response is accurate and relevant. You applied similarity and anomaly detection methods appropriately. You included some comparison of the two perspectives, though it could be deeper. You provided some concrete examples but could have more detail. Some justifications are vague or generic. Formatting could be improved. Minor gaps in explanation.

- **17–22 marks:** Your response has significant issues. Methods are applied but poorly justified. The comparison between similarity and anomaly perspectives is weak or superficial — more like two separate analyses without real integration. Examples from data are sparse or generic. Interpretation doesn't connect well to the specific dataset. Formatting is poor. Missing crucial details. **Submissions in this band typically contain generic observations that could apply to any text dataset** — this indicates insufficient engagement with the specific data.

- **16 marks:** A pass. Methods are barely applied. Little to no comparison of perspectives. No concrete examples from data. Generic observations that could apply to any dataset. Response resembles content copy-pasted from the web or AI chatbot without adaptation.

- **<16 marks:** No answer provided, response is very inadequate, or missing key required elements (e.g., no anomaly detection, no comparison).

## Part B: Research Question (60 marks)

- **>43 marks:** Besides being correct, precise, excellently formatted, and well-explained, you formulated a compelling research question distinct from Part A with clear stakeholder relevance. You applied sophisticated unsupervised learning methods (at least two distinct techniques) with excellent justification for why these methods suit your question and dataset. Most importantly, you provided **detailed analysis with concrete examples**, i.e specific findings from your data with document excerpts, cluster descriptions, topic examples, or pattern illustrations. Your interpretation ties methods to the narrative and shows deep understanding of what the analysis reveals about social phenomena. Your limitations discussion is honest and specific (not generic "more data would help"), showing what your methods capture and what they miss. Your ethics discussion is thoughtful and considers multiple dimensions. Code (when provided) aligns with course style, is well-documented, and produces insights beyond basic outputs.

- **43 marks:** Your response is well-structured and covers all requirements concisely. Research question is clear, appropriate for unsupervised learning, and distinct from Part A. You explained clearly why unsupervised rather than supervised learning is appropriate. Methods are well-chosen and justified specifically for your dataset and question. You provided **concrete examples from your findings**, i.e showing specific patterns, clusters, topics, or anomalies you discovered with illustrative detail. Interpretation is dataset-specific and avoids generic explanations. Limitations discussion is thoughtful and specific. Ethics discussion shows genuine engagement. Code (when provided) is well-documented. Markdown formatting is excellent.

- **34–42 marks:** Your response is accurate and relevant. Research question is appropriate, though may have minor overlap with Part A. Methods are applied competently with reasonable justification. You provided some concrete examples but could have more detail or specificity. Interpretation is mostly dataset-specific with some generic elements. Limitations are addressed but could be more specific. Ethics is discussed but somewhat superficial. Some minor gaps in explanation or formatting.

- **25–33 marks:** Your response has significant issues. Research question may substantially overlap with Part A or not be well-suited to unsupervised learning. Methods are applied but poorly justified or don't clearly connect to the question. Few concrete examples from data; mostly generic observations. **Submissions in this band typically fail to justify method or parameter choices** — why this value of k, this number of topics, this distance metric? Interpretation is superficial and could apply to any dataset. Limitations are generic platitudes. Ethics is perfunctory or checkbox exercise. Formatting is poor. Missing crucial details.

- **24 marks:** A pass. Research question is vague or essentially repeats Part A. Methods barely connect to question. No concrete examples from data. Generic observations throughout. Limitations are "more data would help" type statements. Ethics is missing or completely generic. Response resembles content copy-pasted from web or AI without adaptation.

- **<24 marks:** No answer provided, response is very inadequate, irrelevant to the question, or missing key required elements (e.g., no research question, no limitations discussion, no ethics discussion).

## Key Criteria for High Marks

To achieve distinction-level marks (70+), your work must demonstrate:

1. **Concrete examples and detail**: Don't just say "I found 3 clusters". Describe what's IN those clusters with specific document examples, representative terms, or illustrative cases. Show us, don't just tell us.

2. **Deep justification of methods and parameters**: 
   
   - WHY this method for THIS dataset and question? What perspective does it bring?
   - WHY these parameters? How were they determined? Why are they appropriate for your data?
   - Connect every choice to your analytical goals and data characteristics.
   - **Unjustified parameter choices (e.g., picking k=5 "because it seemed right") will be penalised.**

3. **Dataset-specific insights**: Your interpretation must engage with the specific social context of your data. **Generic observations that could apply to any text dataset will not achieve marks above the lower end of the 2:1 range (max ~62), regardless of how technically competent the analysis is.** For example, "Topic 1 is about food and Topic 2 is about health" is not an insight. Explaining *why* those topics emerge and what they reveal about the domain is.

4. **Concrete, dataset-specific limitations**: 
   
   - Not "more data would help" but specific issues you encountered or trade-offs you made
   - Problems revealed by YOUR analysis of YOUR data
   - What your methods captured and what they missed in THIS context

5. **Thoughtful, grounded ethics discussion**:
   
   - Specific ethical issues arising from YOUR dataset and YOUR findings
   - Consider concrete harms or misuses particular to your analysis
   - Who specifically might be affected by your work?

6. **Code that demonstrates your methods**: Some working code is expected to show how you implemented your analysis and generated your findings. Well-documented code enhances your submission, but the focus should be on using code to support your narrative, not code for its own sake. Submissions that only include code and barely feature any explanation or interpretation will be penalized, as will submissions that don't include any code at all or don't include the code necessary to back up your claims. The best submissions use code to generate specific insights that are then explained in the text, with concrete examples from the data. It goes without saying that the purpose of your code chunks must be clear and that your code should be reproducible. If you choose to include code that is not executable (e.g., because it is computationally expensive), you must explain why and include the results/outputs in your submission.

7. **Integration and coherence**: Part A should compare perspectives meaningfully. Part B should tell a coherent analytical story from question through methods to findings. Building on Part A in Part B (when well-justified) demonstrates sophisticated thinking.

## Important: Code and Reproducibility

**Code is expected to support your analysis and demonstrate your methods.** You should include code that:

- Implements your text mining and unsupervised learning methods
- Generates your findings and visualizations
- Supports your narrative with evidence

**Working code demonstrating your methods is required.** For distinction-level work, your code should be well-documented and produce meaningful outputs that support your analysis.

**Acceptable code formats:**

- **Fully executable Python code** (ideal — runs when we render your `.qmd`)
- **Non-executable code chunks with results shown** (fully acceptable for high marks if computationally expensive — you must explain why code is set to not execute and include the results/outputs)
- **Pseudo-code or proof-of-concept** (acceptable for explaining approach before implementation, or for supplementary analyses where you encountered bugs — explain what you intended. Note: your main analysis must use working code, but occasional pseudo-code for supplementary ideas is fine)

**Code quality matters for high marks:**

- Import all libraries in a single chunk at the start of your document
- Use relative paths that work within your repo structure (not absolute paths like `C:/Users/YourName/...`)
- Follow the `scikit-learn`/`spaCy`/`gensim` patterns taught in the course
- Comment your code to explain what it does and why
- Produce meaningful outputs (not just running code for the sake of it)

**Data and reproducibility:**

- Do NOT upload large data files to your repo
- Provide clear instructions for where to download data and where to place it
- Your code should be reproducible if we follow your instructions

**Penalties will apply for:**

- Not submitting HTML render
- Submitting HTML that is not self-contained (missing images/plots)
- Using absolute paths that break reproducibility
- Importing libraries scattered throughout document instead of at start
- Missing reproducibility instructions for data
- Using AI without acknowledgment (AI use is allowed but must be disclosed in "Use of AI Tools" section)
- Code that produces no meaningful outputs or doesn't support the analysis

## Subsampling Data

You are **allowed to subsample** large datasets for computational reasons. However:

- You must **explain** how and why you sampled
- You must **justify** your sampling approach (random? stratified? time period? why?)
- You must discuss **limitations**. How might sampling affect your results?
- Without this, you will be penalised for unclear methodology

## General Advice

- **Be concise and decisive**: Don't try every method under the sun. Choose methods thoughtfully, justify them, and go deep with interpretation. Verbose submissions that repeat themselves will score lower, not higher.
- **Show concrete examples**: The best responses show us specific findings from the data, not just summaries.
- **Tie methods to narrative**: Every method should serve your analytical story and be justified in context.
- **Think about stakeholders**: Remember your scenario: you're providing insights to inform decisions. What do they need to know?
- **Be honest about limitations**: Good researchers acknowledge what their methods can and cannot tell us.
- **Consider ethics seriously**: This is not a checkbox. Think genuinely about implications.

# How to get help and collaborate with others

## 🙋 Getting help

You can post general clarifying questions on Slack.

For example, you can ask:

- _"I'm working with the Glassdoor dataset and my spaCy pipeline is running very slowly on the full corpus. What's a reasonable subsample size for topic modeling?"_
- _"What's the best way to separate violation codes from inspector comments in the Chicago food inspections data?"_

You **cannot** post questions that reveal your specific approach, analysis, or findings.

You won't be penalized for posting something on Slack that violates this principle without realizing it. We will delete your message and let you know.

## 👯 Collaborating with others

You are allowed to discuss the assignment with others and work alongside each other. However:

- You **cannot** share or copy code
- You **cannot** share your specific analytical approach or findings
- You **cannot** work together on the same analysis
- You **can** discuss general concepts, technical problems, or dataset characteristics
- You **can** help each other troubleshoot Python errors or technical issues

## 🤖 Using AI help?

You can use Generative AI tools such as ChatGPT, Claude, or GitHub Copilot when doing this assignment and you can search online for help. 

**However:**

1. **You must report any AI use.** Add a section at the end of your notebook titled "Use of AI Tools" that describes:
   
   - Which tool(s) you used
   - What you used them for
   - Approximately how much you relied on them

2. **Be aware of AI limitations:**
   
   - AI tools often generate plausible-sounding responses that are incorrect
   - They tend to produce generic, formulaic responses that limit your chances for a high mark
   - For coding, they often generate inefficient code that doesn't follow the principles we teach
   - They cannot understand your specific dataset context as well as you can

3. **AI use will not excuse errors.** If you submit incorrect code or analysis based on AI suggestions, you are responsible for those errors.

**Examples of reporting AI use:**

> "I used ChatGPT to help debug an error in my `spaCy` pipeline where the tokenizer was not handling special characters correctly. I also used it to get a second explanation of how DBSCAN's `eps` parameter works after reviewing the lecture notes."

> "I used GitHub Copilot for code completion throughout the assignment. It helped with syntax but I wrote all the analytical logic myself."

> "I did not use any AI tools for this assignment."

For the full AI use policy and to see examples of how to report the use of AI tools, see 🤖 [Our Generative AI policy](https://lse-dsi.github.io/DS202/2025-2026/winter-term/generative-ai.html).

---

**Good luck! 🍀**

