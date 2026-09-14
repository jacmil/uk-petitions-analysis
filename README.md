# UK Parliamentary Petitions: Topic Structure, Engagement, and Moderation Language

Unsupervised analysis of 11,662 UK parliamentary petitions, asking which issues attract public
engagement and whether the language a petition uses relates to whether it passes moderation.

**[Read the full report](https://jacmil.github.io/uk-petitions-analysis/)** (rendered Quarto
notebook with all code, figures, and interactive plots).

## The question

The petition platform is meant to give the public a direct channel to government. Petitions
clearing 10,000 signatures get a written response; 100,000 gets debate consideration. This
analysis establishes topic groups within the corpus, measures engagement across them, and then
compares the language of rejected against passed petitions within those groups.

## Data

Full corpus of 11,662 petitions from a single parliamentary session, sourced from the UK
Parliament petitions API. Fields used are `action`, `background`, and `additional_details`,
concatenated into one document per petition, which raises average document length from about 50
words to 115. Petitions missing `additional_details` were dropped (570 rows, under 5% of the
corpus, checked against state and signature count for systematic missingness).

`government_response_body`, `rejection_details`, and `debate_overview` were excluded because each
exists only for a small and inherently biased subset.

## Method

**Part A, representation and anomalies.** Sentence-transformer embeddings and TF-IDF, UMAP for
dimensionality reduction, pairwise cosine similarity, and isolation-forest anomaly detection.

**Part B, topics and keyness.** BERTopic over precomputed embeddings, with HDBSCAN clustering and
c-TF-IDF topic labelling. Log-likelihood keyness analysis comparing rejected against passed
petitions within topics, and petitions above against below the 10,000 signature threshold.

BERTopic was chosen over LDA because the topic count was not known in advance. Tuning is
documented in the report: defaults produced 229 topics, most holding only 10 documents, with 21.9%
outliers. Raising `min_cluster_size` to 50 gave 55 usable topics at 29.6% outliers. UMAP
`n_neighbors=30` was tested and rejected because it merged Ukraine/Russia with Gaza/Israel and
collapsed the roads and driving topics into one 724-document catch-all.

## Findings

**Engagement is concentrated.** Every one of the top 15 topics by average signatures per petition
has at least one petition past 100,000 signatures. None of the bottom 15 has a single petition
past 10,000.

**Averages hide the mechanism.** Digital ID averages 29,134 signatures across 104 petitions, but
its median is 9.5, because one petition holds over 3 million. NHS prescriptions has the highest
median at 69, indicating broad sustained signing rather than one viral moment. The platform's
thresholds do not distinguish between these.

**High-rejection topics are locked out.** Rejection rates range from 26.9% (NHS prescriptions) to
94.8% (honours). No topic above roughly 70% rejection has any petition clearing 10,000 signatures
(r = -0.411 against the share clearing 10k). Some of this is mechanical, since rejected petitions
never collect signatures, but the effect is that those issue areas cannot trigger a government
response regardless of latent public support.

**Framing separates rejected from passed, across every topic.** "Think" and "believe" are
overrepresented in passed petitions in virtually every topic, from housing to knife crime to
pensions. Because the pattern holds within topics, it is a platform-level effect rather than
certain subjects attracting more measured language. Topic-specific filters sit on top: elections
rejects partisan language, knives rejects deregulation asks.

Part A found petition language to be semantically homogeneous (mean pairwise cosine similarity
0.18) with lexical anomalies independent of topic. The keyness result is consistent with that:
"I think the government should ban X" and "ban X now" sit close in embedding space, so semantic
methods cannot separate them, while word-frequency methods can. The signal lives in framing rather
than subject matter.

## Limitations

29.6% of petitions fall in BERTopic's outlier group and are excluded downstream, so findings
describe a subset. Signature count conflates genuine interest with campaign infrastructure and
virality. All relationships are correlational. The planned within-topic keyness on signature
thresholds was not possible because no topic had more than 29 petitions above 10,000, so that
comparison was pooled corpus-wide, which mixes topic-level and language-level effects. Findings are
specific to one parliamentary session and to UK Petitions Committee standards.

The report includes a full limitations section and an ethical considerations section covering the
gameability of the framing finding and the risk of the engagement results being read as evidence of
political bias in moderation.

## Running it

```bash
conda env create -f py312-base.yml
conda activate py312
pip install -r requirements-py312.txt
quarto render petitions-analysis.qmd
```


## Context

Solo project, LSE DS202W, spring 2026.
