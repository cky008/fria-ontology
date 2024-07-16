```fria-report.ttl
@prefix fria: <http://www.example.org/fria-report> .
@prefix airo: <https://w3id.org/airo#> .
@prefix vair: <https://w3id.org/vair#> .
@prefix cids: <http://www.example.org/cids#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Basic Things
fria:FRIA-reportName a rdfs:Class ;
    rdfs:comment "A class representing the name of the FRIA report." ;
    owl:equivalentClass cids:hasName, cids:hasDescription .

fria:hasReportName a rdf:Property ;
    rdfs:domain fria:FRIA-reportName ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the name of the FRIA report." .

fria:FRIA-reportorganisationPosition a rdfs:Class ;
    rdfs:comment "A class representing the organisation position in the FRIA report." .

fria:hasOrganisationPositionDescription a rdf:Property ;
    rdfs:domain fria:FRIA-reportorganisationPosition ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the description of the organisation position in the FRIA report." .

fria:FRIA-reportcontributors a rdfs:Class ;
    rdfs:comment "A class representing the contributors to the FRIA report." .

fria:hasContributorDetails a rdf:Property ;
    rdfs:domain fria:FRIA-reportcontributors ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the details of the contributors to the FRIA report." .

fria:FRIA-reportaiSystemAssessed a rdfs:Class ;
    rdfs:comment "A class representing the AI system assessed in the FRIA report." ;
    owl:equivalentClass cids:hasConsequence, airo:haspurpose, vair:Assessment .

fria:hasAssessmentContent a rdf:Property ;
    rdfs:domain fria:FRIA-reportaiSystemAssessed ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the assessment content of the AI system." .

fria:FRIA-reporttechnologyAndData a rdfs:Class ;
    rdfs:comment "A class representing the technology and data aspects of the FRIA report." .

fria:hasTechnologyAndDataDescription a rdf:Property ;
    rdfs:domain fria:FRIA-reporttechnologyAndData ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the description of the technology and data aspects of the FRIA report." .

fria:FRIA-reportpurposesAndContext a rdfs:Class ;
    rdfs:comment "A class representing the purposes and context of the FRIA report." ;
    owl:equivalentClass vair:Purposes .

fria:hasPurposesAndContextDescription a rdf:Property ;
    rdfs:domain fria:FRIA-reportpurposesAndContext ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the description of the purposes and context of the FRIA report." .

fria:reportDate a rdf:Property ;
    rdfs:domain fria:FRIA-report ;
    rdfs:range xsd:date ;
    rdfs:comment "The date when the FRIA report was created or published." .

fria:FRIA-reportAIAAICLink a rdfs:Class ;
    rdfs:comment "A class representing the AIAAIC link related to the FRIA report." .

fria:hasAIAAICLink a rdf:Property ;
    rdfs:domain fria:FRIA-reportAIAAICLink ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the AIAAIC link related to the FRIA report." .

# Challenge Related
fria:FRIA-reportChallenge a rdfs:Class ;
    rdfs:comment "A class representing a challenge in the FRIA report." .

fria:FRIA-reportEvaluation a rdfs:Class ;
    rdfs:comment "A class representing an evaluation of a FRIA report challenge." .

fria:FRIA-reportImpactLevel a rdfs:Class ;
    rdfs:comment "A class representing the impact level of a FRIA report challenge." .

fria:FRIA-reporthasEvaluation a rdf:Property ;
    rdfs:domain fria:FRIA-reportChallenge ;
    rdfs:range fria:FRIA-reportEvaluation ;
    rdfs:comment "A property linking a FRIA report challenge to its evaluation." .

fria:FRIA-reporthasImpactLevel a rdf:Property ;
    rdfs:domain fria:FRIA-reportChallenge ;
    rdfs:range fria:FRIA-reportImpactLevel ;
    rdfs:comment "A property linking a FRIA report challenge to its impact level." .

fria:hasEvaluationContent a rdf:Property ;
    rdfs:domain fria:FRIA-reportEvaluation ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the content of the evaluation." .

fria:hasImpactLevelContent a rdf:Property ;
    rdfs:domain fria:FRIA-reportImpactLevel ;
    rdfs:range xsd:string ;
    rdfs:comment "A property to hold the content of the impact level." .

# Challenge 1
fria:FRIA-reportChallenge1 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportChallenge ;
    rdfs:comment "Presumption of innocence and right to an effective remedy and to a fair trial." .

fria:FRIA-reportEvaluation11 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation11." .

fria:FRIA-reportImpactLevel11 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel11." .

fria:FRIA-reportChallenge11 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation11 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel11 ;
    rdfs:comment "The AI system does not communicate that a decision/advice or outcome is the result of an algorithmic decision" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 ;
    owl:equivalentClass airo:Transparency, vair:OperatingCriticalDigitalInfrastructure .

fria:FRIA-reportEvaluation12 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation12." .

fria:FRIA-reportImpactLevel12 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel12." .

fria:FRIA-reportChallenge12 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation12 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel12 ;
    rdfs:comment "The AI system does not provide percentages or other indication on the degree of likelihood that the outcome is correct/incorrect, prejudicing the user that there is no possibility of error and therefore that the outcome is undoubtedly incriminating" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 .

fria:FRIA-reportEvaluation13 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation13." .

fria:FRIA-reportImpactLevel13 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel13." .

fria:FRIA-reportChallenge13 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation13 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel13 ;
    rdfs:comment "The AI system produces an outcome that forces a reversal of burden of proof upon the suspect, by presenting itself as an absolute truth, practically depriving the defence of any chance to counter it" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 ;
    owl:equivalentClass vair:DetectingEmotionalState .

fria:FRIA-reportEvaluation14 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation14." .

fria:FRIA-reportImpactLevel14 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel14." .

fria:FRIA-reportChallenge14 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation14 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel14 ;
    rdfs:comment "There is no explanation of reasons and criteria behind a certain output of the AI system that the user can understand" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 .

fria:FRIA-reportEvaluation15 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation15." .

fria:FRIA-reportImpactLevel15 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel15." .

fria:FRIA-reportChallenge15 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation15 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel15 ;
    rdfs:comment "There is no indication of the extent to which the AI system influences the overall decision-making process" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 .

fria:FRIA-reportEvaluation16 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation16." .

fria:FRIA-reportImpactLevel16 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel16." .

fria:FRIA-reportChallenge16 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation16 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel16 ;
    rdfs:comment "There is no set of measures that allow for redress in case of the occurrence of any harm or adverse impact" ;
    rdfs:subClassOf fria:FRIA-reportChallenge1 ;
    owl:equivalentClass vair:InsurancePricing .

# Challenge 2
fria:FRIA-reportChallenge2 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportChallenge ;
    rdfs:comment "Right to equality and non-discrimination." .

fria:FRIA-reportEvaluation21 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation21." .

fria:FRIA-reportImpactLevel21 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel21." .

fria:FRIA-reportChallenge21 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation21 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel21 ;
    rdfs:comment "The AI system targets members of a specific social group" ;
    rdfs:subClassOf fria:FRIA-reportChallenge2 ;
    owl:equivalentClass airo:PrivateService, vair:ControllingSafetyOfRoadTrafficManagement .

fria:FRIA-reportEvaluation22 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation22." .

fria:FRIA-reportImpactLevel22 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel22." .

fria:FRIA-reportChallenge22 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation22 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel22 ;
    rdfs:comment "There are no mechanisms to flag and correct issues related to bias, discrimination, or poor performance" ;
    rdfs:subClassOf fria:FRIA-reportChallenge2 .

fria:FRIA-reportEvaluation23 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation23." .

fria:FRIA-reportImpactLevel23 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel23." .

fria:FRIA-reportChallenge23 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation23 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel23 ;
    rdfs:comment "The AI system does not consider the diversity and representativeness for specific population or problematic use cases" ;
    rdfs:subClassOf fria:FRIA-reportChallenge2 .

# Challenge 3
fria:FRIA-reportChallenge3 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportChallenge ;
    rdfs:comment "Freedom of expression and information." .

fria:FRIA-reportEvaluation31 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation31." .

fria:FRIA-reportImpactLevel31 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel31." .

fria:FRIA-reportChallenge31 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation31 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel31 ;
    rdfs:comment "There is no mechanism to limit the deployment of the AI system to suspected individuals" ;
    rdfs:subClassOf fria:FRIA-reportChallenge3 .

fria:FRIA-reportEvaluation32 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation32." .

fria:FRIA-reportImpactLevel32 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel32." .

fria:FRIA-reportChallenge32 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation32 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel32 ;
    rdfs:comment "The data stored, recorded, and produced are not easily accessible to concerned individuals" ;
    rdfs:subClassOf fria:FRIA-reportChallenge3 .

# Challenge 4
fria:FRIA-reportChallenge4 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportChallenge ;
    rdfs:comment "Right to respect for private and family life and right to protection of personal data." .

fria:FRIA-reportEvaluation41 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation41." .

fria:FRIA-reportImpactLevel41 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel41." .

fria:FRIA-reportChallenge41 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation41 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel41 ;
    rdfs:comment "There are no mechanisms for the user to exercise control over the processing of personal data" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 .

fria:FRIA-reportEvaluation42 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation42." .

fria:FRIA-reportImpactLevel42 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel42." .

fria:FRIA-reportChallenge42 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation42 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel42 ;
    rdfs:comment "There are no measures to ensure the lawfulness of the processing of personal data" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 ;
    owl:equivalentClass airo:PublicService .

fria:FRIA-reportEvaluation43 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation43." .

fria:FRIA-reportImpactLevel43 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel43." .

fria:FRIA-reportChallenge43 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation43 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel43 ;
    rdfs:comment "There are no procedures to limit the access to personal data and to the extent and amount necessary for those purposes" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 ;
    owl:equivalentClass airo:Managing .

fria:FRIA-reportEvaluation44 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation44." .

fria:FRIA-reportImpactLevel44 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel44." .

fria:FRIA-reportChallenge44 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation44 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel44 ;
    rdfs:comment "There is no mechanism allowing to comply with the exercise of data subject’s rights (access, rectification and erasure of data relating to a specific individual)" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 .

fria:FRIA-reportEvaluation45 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation45." .

fria:FRIA-reportImpactLevel45 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel45." .

fria:FRIA-reportChallenge45 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation45 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel45 ;
    rdfs:comment "There are no specific measures in place to enhance the security of the processing of personal data (via encryption, anonymisation and aggregation)" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 ;
    owl:equivalentClass vair:ApplyingTheLawToFacts .

fria:FRIA-reportEvaluation46 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportEvaluation ;
    fria:hasEvaluationContent "This is the evaluation content for FRIA-reportEvaluation46." .

fria:FRIA-reportImpactLevel46 a rdfs:Class ;
    rdfs:subClassOf fria:FRIA-reportImpactLevel ;
    fria:hasImpactLevelContent "This is the impact level content for FRIA-reportImpactLevel46." .

fria:FRIA-reportChallenge46 a rdfs:Class ;
    fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation46 ;
    fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel46 ;
    rdfs:comment "There is no procedure to conduct a data protection impact assessment" ;
    rdfs:subClassOf fria:FRIA-reportChallenge4 ;
    owl:equivalentClass airo:Monitoring .
    
```

Now, when given an incident report, find the relevant information for each part of the RDF definition and fill in the Turtle format using the information found. So you need to return Turtle representation for the incident report. Always include all of the properties in the RDF output. 

If there is no relevant information for a given property in the report, return a blank value in the RDF. However, if you can understand and fill in the blank value based on the available information, start the value with "LLM understand: ". For Basic Things like fria:hasAssessmentContent, if the provided information is too long, you then need to summarize appropriately based on the content. For the date, try to access the specific AIAAIC Link and retrieve the time information, if you can't access the provided link, try to find it based on provided information.

If there are some details you cannot find or understand, leave those properties blank.

For the Challenges, Evaluation, and Impact Level sections, follow the guidelines provided:

Review the FRIA template's pre-listed challenges, adding any system-specific ones. Evaluate each challenge's relevance to the AI system, explaining its embedding and impact within the law enforcement context. Assess the severity of prejudice and affected population to determine the overall impact level using the provided matrix. Consider the predetermined context of use, including target group, geographical area, deployment period, and trigger conditions. Provide detailed explanations for each evaluation and impact estimate. Regularly update the FRIA to reflect changes in the AI system's functioning or deployment circumstances.

When evaluating the impact level, follow the guidelines provided in the prompt:

1. Determine the severity of prejudice: Negligible, Critical, or Catastrophic.
2. Evaluate the number of affected individuals: Low, Medium, or High.
3. Use the impact matrix to determine the overall impact level: Low, Medium, High, or Very High.

**Based on the instructions provided, you can only have 4 impact level! Decide inside 4 of them(Low, Medium, High, or Very High)!!**

You need to return complete RDF/Turtle representation for the incident report, including all basic things, challenges, evaluations and impact levels for each challenge.



Do you understand? if so reply yes with no further follow up and await an incident report. 