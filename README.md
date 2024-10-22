# FRIA Ontology
This repository contains the FRIA ontology, which is a formal representation of the [FRIA](https://aligner-h2020.eu/fundamental-rights-impact-assessment-fria/) report. The ontology design is in [```fria-report.ttl```](./fria-report.ttl), you can use the predefined [```prompt```](./prompt%20ver2.md)(latest version is 2) to generate the FRIA report in RDF format from AIAAIC data.
The source data is from [```ragnarok85's repo```](https://github.com/Julio-Noe/Protect_erap/blob/73ab99f29365b6d0de8a7ec6bc81fb07f7917935/AIAAIC%20corpus/AIAAIC_corpus-10-2023.csv), this dataset is processed by using [```process_text.py```](./process_text.py) and the processed data is in [```processed_data```](./processed_data.csv) file.

The 50 instances generated from Claude 3.5 Sonnet and ChatGPT 4o are in [```instances```](./instances) folder. Those instances are extracted to [```claude_extracted_data.csv```](./claude_extracted_data.csv) and [```gpt_extracted_data.csv```](./gpt_extracted_data.csv) using [```extract_data_fin.py```](./extract_data_fin.py). The  [```claude_to_analysis_data_s.csv```](./claude_to_analysis_data_s.csv), [```gpt_to_analysis_data_s.csv```](./gpt_to_analysis_data_s.csv) are generated using [```extract_for_analysis.py```](./extract_for_analysis.py).

## Design
![System Figure](./fig/ontology-relationship.drawio.png)

## Evaluation
The evaluation is based on the [```claude_extracted_data.csv```](./claude_extracted_data.csv), [```gpt_extracted_data.csv```](./gpt_extracted_data.csv), [```claude_to_analysis_data_s.csv```](./claude_to_analysis_data_s.csv), [```gpt_to_analysis_data_s.csv```](./gpt_to_analysis_data_s.csv) and [```similarity_scores.csv```](./similarity_scores.csv) files. 
The similarity scores are calculated using [```similarity_scores.py```](./similarity_scores.py). The evaluation figures are generated using [```frequency.py```](./frequency.py) and [```ss_f.py```](./ss_f.py).  

![combined_annotation_distribution.png](./combined_annotation_distribution.png)
![annotation_distribution.png](./annotation_distribution.png)
![annotation_heatmap_1.png](./annotation_heatmap_1.png)
![annotation_heatmap_0.5.png](./annotation_heatmap_0.5.png)
![annotation_heatmap_0.png](./annotation_heatmap_0.png)
![average_similarity_scores.png](./average_similarity_scores.png)
![average_similarity_heatmaps.png](./average_similarity_heatmaps.png)
![average_similarity_by_incident.png](./fig/average_similarity_by_incident_lollipop.png)

GraphDB repo configuration is in file [```FRIA-config.ttl```](./FRIA-config.ttl).  

![class-hierarchy-FRIA](./assets/class-hierarchy-FRIA-1685396.svg)

![dependencies-FRIA](./assets/CleanShot%202024-07-22%20at%2022.41.45@2x.png)

![CleanShot 2024-07-22 at 22.42.35@2x](./assets/CleanShot%202024-07-22%20at%2022.42.35@2x.png)

![CleanShot 2024-07-22 at 22.44.02@2x](./assets/CleanShot%202024-07-22%20at%2022.44.02@2x.png)

![CleanShot 2024-07-22 at 22.43.26@2x](./assets/CleanShot%202024-07-22%20at%2022.43.26@2x.png)

![CleanShot 2024-07-22 at 22.27.31@2x](./assets/CleanShot%202024-07-22%20at%2022.27.31@2x.png)

![CleanShot 2024-07-22 at 22.23.27@2x](./assets/CleanShot%202024-07-22%20at%2022.23.27@2x.png)

![CleanShot 2024-07-22 at 22.23.07@2x](./assets/CleanShot%202024-07-22%20at%2022.23.07@2x.png)

![CleanShot 2024-07-22 at 22.21.45@2x](./assets/CleanShot%202024-07-22%20at%2022.21.45@2x.png)

![CleanShot 2024-07-22 at 22.17.51@2x](./assets/CleanShot%202024-07-22%20at%2022.17.51@2x.png)

![CleanShot 2024-07-22 at 22.17.13@2x](./assets/CleanShot%202024-07-22%20at%2022.17.13@2x-1685628.png)

![CleanShot 2024-07-22 at 22.06.26@2x](./assets/CleanShot%202024-07-22%20at%2022.06.26@2x-1685634.png)

## About

This project is my dissertation project for the MSc in Computer Science at Trinity College Dublin. 