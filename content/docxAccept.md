---
title: "When is a Picture Worth 1,000 SNPs: Effects of User-Submitted Photographs on Ancestry Estimates from Direct-to-Consumer Canine Genetic Tests"
---

This manuscript was automatically generated on April 8, 2023.

## Abstract

This will be written later.

## Introduction

The study of genetic disease in animal models has a long history, and commercial genetic testing has been used to guide agricultural breeding practices for over 20 years \[[1]\]. Animal genetic testing is a booming industry, expected to grow over the next five years \[[2]\]. Commercial testing for genetic risk factors has been common for dogs \[[3]\] and cats \[[4]\] for over a decade. Over that same time, direct-to-consumer (DTC) genetic testing for humans has grown into an established industry \[CITE\]. Such genetic tests require consumers to collect a specimen (usually a buccal swab) at home and ship it to the company where it will be sequenced and processed. The individual receives a report containing information about their ancestry and, in some cases, the likelihood of possessing certain genetic traits (e.g., hair color) and risk of developing various genetic diseases.

Perhaps unsurprisingly, a parallel industry of DTC genetic profiling of companion animals, primarily dogs, has also emerged. For these companion tests, consumers are instructed to collect a buccal swab from a pet instead of swabbing their own cheek. That pet sample is then shipped to the company, which sequences and analyzes it. The sample is analyzed for ancestry (breed) and/or genotypes associated with certain traits or diseases. The consumer receives a report containing this information, similar to the human DTC equivalent. Dogs were the first domesticated animal \[CITE\], and dog husbandry has a rich history \[CITE\], and as a result, the genetic signature of dog breeds is more distinct than in many other species. Additionally, dog breeds are, in the strict sense, closed breeding populations due to dog husbandry practices, and so dog breed ancestry can be estimated based on genetic variants associated with specific breeds. Therefore, the ability of a dog breed ancestry test to assign breed(s) depends on two variables: first, the density of genetic markers analyzed, and second, the breed coverages and diversity of individuals from within each breed available to compare against. Most DTC genetic tests assay single-nucleotide polymorphisms (SNPs) using a microarray, or "chip," while a few use whole-genome sequencing or copy-number variation, presumably of short-tandem repeats (STRs) (Table ??). The genetic variations observed in an individual dog is then compared against a panel of genetic variants from a variety of breeds and individuals using algorithms that are typically proprietary. However, most approaches use unsupervised clustering and similarity metrics comparing their existing training data (sometimes including results from previous DTC tests) to the new dog sample. This approach allows for classification of the individual's genetic variants to assign one or more breeds, which can then be deconvolved into measured sources of genetic ancestry.

**Comparison of six DTC dog genetic testing services.** At the time of study design (end of 2021), 6 DTC dog tests were available on the public market. All 6 were included in this study. To the extent that the information is available, each test uses a distinct combination of genotyping technologies, breed classification algorithms, and reference panels (see {#tbl:tests}). While this study focuses on the methodologies, a detailed breakdown of consumer-oriented similarities and differences among several of these tests is available elsewhere \[[5]\]. {#tbl:tests}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Test/Company Name                                 Price of Base Breed Test   Markers Used                                                                                            Reference Panel                            Ancestry Assignment Algorithm
  ------------------------------------------------- -------------------------- ------------------------------------------------------------------------------------------------------- ------------------------------------------ -------------------------------
  Embark Breed Test                                 \$129-\$199                200,000+ SNPs, CanineHD SNP chip with additional probes                                                 350+ breeds                                Not specified

  Wisdom Panel Breed Discovery                      \$80-\$160                 SNPs, number not specified, use custom genotyping chip                                                  350+ breeds, 21,000+ samples \[[6],[7]\]   BCSYS

  Orivet GenoPet                                    \$95-160                   SNPs, number not specified \[[8]\]                                                                      320+ breeds \[[9]\]                        Not specified

  Darwin's Ark Explorer Level Donation              \$149 donation             Call millions of SNPs from whole-genome sequencing, use 688,060 for breed mix classification \[[10]\]   101 breeds                                 SupportMix \[[11]\]

  DNA My Dog Essential Breed ID Test                \$80-\$130                 Copy-number variation, number of markers not specified \[[12]\]                                         350+ breeds                                Not specified

  Accu-Metrics/Via-Pet Canine Breed Determination   \$59                       Not specified                                                                                           340 breeds \[[13]\]                        Not specified
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Because the methodologies used to assign ancestry and the make-up of the comparison panels are likely to differ, it is expected that results would typically vary across tests. However, crowd-sourced results, as available through the "DoggyDNA" subreddit \[[14]\], suggest that some users receive wildly different results, beyond what would be expected from the known methodologic differences. In investigating such discrepancies, we noted that most of the DTC tests either include the option for or require the user to upload a photograph, despite the tests being advertised as based on genetics only. Depending on how the photographic information is incorporated into the breed identification pipeline, it could potentially bias the results. Therefore, we sought to assess whether the photograph uploaded with a DNA sample influenced breed ancestry estimation by six DTC dog genetic testing companies, in addition to their overall genetic accuracy.

We recruited 12 purebred dogs and submitted their buccal DNA samples along with a photograph to six companies (Table ??). For half the tests, the DNA sample was submitted with a photograph of the DNA donor. For the other half, photos were swapped between dogs so that each DNA sample was submitted with a photograph of a different purebred dog. This design allowed us to evaluate whether the photograph had a significant effect on ancestry estimation. Additionally, we evaluated whether DTC test breed predictions matched the donor's registered breed. In doing so, we are able to provide a formal comparison of differences in breed ancestry estimation across different platforms.

## Methods

Dogs were recruited by word of mouth in several locations between July and November 2022. Breed organization registration of each dog was confirmed through manually viewing the dog's breed organization paperwork or locating the dog in the American Kennel Club (AKC) database. Recruitment was run to ensure full coverage of dog breeds across breed clades (\[15\]). Each dog was randomized to either the control or treatment group, and dogs in the treatment group were paired based on order of enrollment in the study. Group assignments were evaluated to ensure that dogs within a breed clade (per \[[15]\]) were not paired. All enrolled dogs came from different households, ensuring that there could be no cross-contamination of dogs within the study.

DTC genetic tests were purchased directly from each company's website. Kits were registered according to the instructions provided, using the dog's own photograph (control) or the photograph of a paired dog (treatment). The kits were then delivered to the owner, who was instructed to collect buccal swabs for each of the 6 kits in Table ?? according to manufacturer instructions and mail the samples using the company-provided packaging. Genetic testing was conducted by each DTC genetic testing company according to their own protocols. The breed determination results were returned to the authors, who retrieved the results for each dog and recorded all results for the determined breeds and the corresponding percentage composition in a spreadsheet.

Finally, as a positive control for the potential photographic test bias, we evaluated each sample/photograph pair using a pre-trained convolutional neural network, to predict breed. Dog breed classification is a classic problem in computer vision, and models trained on images from a large compendium (ImageNet) have been evaluated for their performance in classifying photographs of purebred dogs, with the model NASNet showing particularly robust performance \[[16],[17],[18]\]. Therefore, NASNet complements DTC genetic testing results by predicting breeds based on photograph exclusively. We loaded the NASNet model nasnetalarge from the Python package PyTorch Image Models (timm version 0.6.12) \[[19]\] and used to classify each of the dog photos. The classifier provides estimates for a large number of categories with a very long tail, and so only results with a score greater than 1% were included in the analysis.

To evaluate whether swapping the photographs affected breed prediction for each DTC test, the proportion of results matching the registered breed across the two conditions was compared by calculating the odds ratio. In cases where a test had either zero matching or zero non-matching predictions within a condition (i.e., one or more zero cells), the Haldane-Anscombe correction \[[20]\] was applied per \[[21],[22]\]. The probability of both the treatment and control results coming from the same distribution was evaluated using a one-tailed Fisher's exact test. Both statistical tests were conducted in R using the package vcd \[[23]\].

Based on qualitative patterns observed in the results, the decision was made *post hoc* to compare the phylogenetic clades \[[15]\] of predicted breeds to those of the registered breeds of the DNA donor and photographed dogs. Each breed was mapped onto a clade, as identified by \[[15]\] or based on its close genetic relationship to breeds assigned to clades in \[[15]\]. In the treatment condition, the clade of each predicted breed was then compared to the clades of the DNA donor versus the dog whose photograph was provided to the testing company. In the control condition, dogs were paired with another dog based on the order in which they were recruited. The breed predictions were then evaluated to determine whether their clade matched the clade of the photographed or paired dog (in the treatment and control conditions, respectively). The goal of this analysis was to evaluate whether results that matched neither the registered breed of the DNA donor nor the photograph provided were closely related to, but not identical to, the photographed dog. Odds ratio and Fisher's exact test were applied using the vcd package in R. Additionally, the results at the level of breed clade were plotted in R using the ternary package \[[24]\].

## Results

Twelve purebred dogs were recruited from households around the United States and sampled by their owners (Table [1][25]). Results were returned from the DTC genetic testing companies between August 2021 and February 2023. For all dogs, at least one DTC test returned a result 100% consistent with the registered breed, and the registered breed was always the majority estimate (Figure [1][26]).

[]{#tbl:subjects .anchor}Table 1: **Background information on the twelve canine participants.** All dogs were registered with a breed organization (AKC = American Kennel Club; UKC = United Kennel Club; CKC = Continental Kennel Club). Breed clade was assigned based on phylogeny \[[15]\] as opposed to the breed groups used by breed organizations such as the AKC.

  ------------------------------------------------------------------------------------------------------------------
  Breed                         Breed Clade        Registry Organization   Condition   Photograph
  ----------------------------- ------------------ ----------------------- ----------- -----------------------------
  Beagle                        Scent Hound        UKC                     Control     Self

  Border Terrier                Terrier            AKC                     Control     Self

  Golden Retriever              Retriever          AKC                     Control     Self

  Pomeranian                    Small Spitz        AKC                     Control     Self

  Shetland Sheepdog             UK Rural           AKC                     Control     Self

  Shih Tzu                      Asian Toy          CKC                     Control     Self

  Brittany Spaniel              Pointer/Setter     AKC                     Treatment   Chinese Crested Dog

  Chinese Crested Dog           American Toy       AKC                     Treatment   Brittany Spaniel

  German Short-Haired Pointer   Pointer/Setter     AKC                     Treatment   Italian Greyhound

  Italian Greyhound             UK Rural           AKC                     Treatment   German Short-haired Pointer

  English Bulldog               European Mastiff   AKC                     Treatment   Labrador Retriever

  Labrador Retriever            Retriever          AKC                     Treatment   English Bulldog
  ------------------------------------------------------------------------------------------------------------------

In some cases, terminology needed to be harmonized across studies. For example, the term "British Bulldog" was used by Orivet to describe what the AKC and other DTC tests termed a "Bulldog" \[[25]\]. Similarly, the tests reported results in somewhat different ways. While most tests provided quantitative estimates of ancestry (e.g., 15.5% German Shepherd Dog), DNA My Dog and Accu-Metrics both provide a qualitative result (e.g., 10-20% German Shepherd Dog). These range-format estimates were converted to approximate numeric estimates for visualization purposes (i.e., Figure [1][26]). Another difference in the way results were reported across tests was that Darwin's Ark provided a formal breed prediction that did not necessarily match the ancestry percentage estimates; this was achieved by evaluating ancestry and genetic diversity separately, allowing them to explicitly identify whether a dog was likely to be purebred. We used these determinations, rather than the percentages (Figure [1][26]), to assess whether Darwin Ark's result matched the registered breed (Table [2][27]). Because our our analysis focused on evaluating whether the reported ancestry deviated from the expected ancestry, which due to study design was always 100% of a single breed (purebred), minor differences in how results were reported by different companies did not affect our analyses. Most tests returned at least one result that did not match the dog's breed organization registration. The only exceptions to this were Wisdom Panel, which always estimated the registered breed to be 100% of the ancestry, and Darwin's Ark, which was always able to discern that the donor was purebred based on lower genetic diversity (Table [2][27]).

[]{#fig:pies .anchor}![Figure 1: Breed ancestry predictions from six DTC dog genetic testing companies as well as a pretrained image classifier.]

Figure 1: **Breed ancestry predictions from six DTC dog genetic testing companies as well as a** **pretrained** **image classifier.** For the control condition, the breeds of the donor and photograph match, so the registered breed is depicted as purple. In the treatment condition, these are separated into blue (DNA donor) and red (photographed breed). All other breeds are represented in other colors as identified in the legend.

[]{#tbl:accuracy .anchor}Table 2: **Comparison of six DTC genetic tests and one pretrained image classifier (NASNet) to the registered breed of each dog.** The overall concordance with breed registration is reported, as well as the breakdown between the two conditions. The Haldane-Anscombe correction was applied when one or more cells was zero. p-values were calculated using Fisher's exact test. Note: for Orivet, the conditions were not balanced because, due to experimenter error, one control subject (Golden Retriever) was submitted with two photographs, the photograph of the DNA donor and of another dog (Pomeranian).

  --------------------------------------------------------------------------------------------------------
  Algorithm      Overall Results Matching Breed   Control Matching   Treatment Matching   Odds Ratio (p)
  -------------- -------------------------------- ------------------ -------------------- ----------------
  Embark         10/12 (83%)                      5/6 (83%)          5/6 (83%)            1 (0.773)

  Wisdom Panel   12/12 (100%)                     6/6 (100%)         6/6 (100%)           1 (1.00)

  Orivet         7/9                              2/3                5/6                  

  DNA My Dog     8/12 (67%)                       4/6 (67%)          4/6 (67%)            1 (0.727)

  Darwin's Ark   11/11                            6/6 (100%)         5/5                  

  Accu-Metrics   0/8                              0/4                0/4                  

  NASNet         2/12 (17%)                       2/6 (33%)          0/6 (0%)             7.22 (0.227)
  --------------------------------------------------------------------------------------------------------

Upon receiving the results, we noted that the primary outcome selected *a priori* did not capture apparent qualitative differences (Figure [1][26]). This discrepancy appeared to be driven by the fact that in several cases, the breeds predicted matched neither the DNA nor the photograph. This pattern was particularly apparent for the image classifier and for one DTC test (ViaPet by Accu-Metrics). In the case of the neural network, this was likely influenced in part by the fact that not all breeds have been labeled in ImageNet \[[26]\]. In the case of the genetic test, it may have been influenced by the fact that the test predicted the registered breed zero times across both the control and treatment conditions (Table [2][27]). Re-evaluating the results at the level of breed clades (Figure [2][28]) revealed that, for both tests, the predicted breeds were more similar to the photograph than to the DNA sample, suggesting that the Accu-Metrics test used the dog's photographs in their analysis. The effect of the treatment was significant, as expected, on the similarity of NASNet's predictions to the DNA donor (OR = 169). In the case of Accu-Metrics... (update when more results are back).

[]{#fig:tern .anchor}![Figure 2: Ternary plots identifying the breed clades of results predicted by each test. Each dog is represented by a circle in blue (control) or red (treatment). The position of the circle relative to the three axes indicates the percentage of results belonging to the breed clade of the DNA donor, photographed dog, or other clades. A result that is 100% concordant with the DNA donor's registered breed will be placed at the apex of the triangle. A result that is 100% concordant with the photographed dog's breed (in the treatment condition only) will be located at the top left. Offset from these positions can be interpreted by looking at the position relative to the other two vertices on a 0 to 100 scale. Darker colors indicate multiple circles mapping to the same position.]

Figure 2: **Ternary plots identifying the breed clades of results predicted by each test.** Each dog is represented by a circle in blue (control) or red (treatment). The position of the circle relative to the three axes indicates the percentage of results belonging to the breed clade of the DNA donor, photographed dog, or other clades. A result that is 100% concordant with the DNA donor's registered breed will be placed at the apex of the triangle. A result that is 100% concordant with the photographed dog's breed (in the treatment condition only) will be located at the top left. Offset from these positions can be interpreted by looking at the position relative to the other two vertices on a 0 to 100 scale. Darker colors indicate multiple circles mapping to the same position.

## Discussion

This study applied an experimental paradigm to assess the state of the DTC dog genetic testing industry and revealed qualitative and quantitative differences in the breed ancestry estimates of six DTC dog genetic tests. By modulating whether DNA was submitted with a matched or mis-matched photograph, we evaluated whether this non-genetic information influenced the breed predictions made by different DTC dog genetic testing services. Using a pre-trained convolutional neural network, NASNet, allowed for these predictions to be compared to those made based on the photograph alone. Ultimately, this analysis demonstrated a low rate of consensus across tests in estimating the breed makeup even of registered purebred dogs, and suggested that results from at least one company are influenced by the photograph provided.

Most DTC testing services had a very high rate of predicting the registered breed of the DNA donor, regardless of condition. Unsurprisingly, the statistical analysis did not support an effect of condition on the chance that these tests would return the registered breed of the DNA donor. However, both NASNet and one DTC test, Accu-Metrics, showed the opposite pattern: they were unlikely to identify the registered breed as 100% of the ancestry, regardless of condition. Instead, when breed ancestry estimates were evaluated at the clade level, a significant effect of the photograph the results of NASNet and Accu-Metrics became apparent, with the clades of the predicted breeds being very likely to match that of the photograph (Figure [2][28]). This result was expected for NASNet, but suggests that Accu-Metrics breed predictions are influenced by the photograph.

It is important to note that this study did not evaluate the genetic accuracy of the tests. This point is especially important to note in the context of tests with extremely high performance. While Wisdom Panel returned a prediction that matched the DNA donor's registered breed 100% of the time, this does not mean that it was more accurate than Embark or Orivet. Differences among tests such as the number of markers analyzed (Table ??) are expected to result in differences in resolution, and therefore result in differences in breed prediction. As a specific example, Embark identified 5.5% American Foxhound DNA in the Labrador Retriever evaluated, suggesting a Foxhound ancestor approximately 5 generations ago. This individual dog's pedigree indicates that 6 of her 16 great-grandparents were enrolled in the AKC's Voluntary DNA Profile Program, which allows breeders to confirm the parentage of their dogs. Therefore, the foxhound admixture is unlikely to come from these 6 ancestors. However, among the remaining 10 great-grandparents, it is possible that one had mistaken parentage and an American Foxhound parent, especially since Embark's chromosome chart for this dog suggested inheritance of Foxhound ancestry from only one of her parents. In fact, the other high-resolution test, Darwin's Ark, estimated a similar amount (5.9%) of non-Labrador ancestry for this dog. However, Darwin's Ark does not currently include the American Foxhound in its reference panel, and instead assigned this non-Labrador ancestry to Viszla (3.0%) and unknown (2.9%). Without a third test to compare, or a foxhound DNA panel, it is impossible to know which test is accurate. Therefore, this is a clear illustration both of the influence of the reference panel on what breeds as assigned and of the fact that it is difficult to evaluate the accuracy of these tests, even for purebred dogs.

We can, however, conclude from our results that at least one dog DTC genetic test is not providing accurate information about genetic ancestry. Results from this test were demonstrably influenced by the photographs provided. Further investigation would be required to assess accuracy among the remaining five genetic tests. For example, one test result indicated that the purebred Bulldog had 10-20% wolf ancestry. This result would be consistent with a full wolf ancestor three generations ago. While the authors did not have access to this dog's four-generation pedigree, it would be surprising that such a high amount of wolf ancestry would be missed by other tests. Because the test that produced this result, DNA My Dog, uses copy number variation (presumably STRs), it is possible that different genetic tools tell different stories. Therefore, these findings suggest that methodological literacy is important to interpreting the results of DTC tests, but the average consumer is unlikely to have the information or training to critically evaluate these features.

Lack of genetic literacy when provided DTC test results could be concerning because dog breed ancestry can have social and economic consequences for owners. For example, many home insurance companies refuse to cover certain dog breeds such as pitbulls and rottweilers. In our current sample of twelve purebred dogs (none of which are banned by more than 5% of insurance companies \[[27]\]), two dogs were identified as having ancestry banned by more than 50% of companies. DNA My Dog identified the Bulldog as a wolf hybrid and the Beagle as part Rottweiler, and Accu-Metrics identified both the German Short-Haired Pointer and Golden Retriever as part American Staffordshire Terrier. None of these ancestry predictions were supported by any other DTC tests. Therefore, it would be possible for dog owners to face severe financial repercussions in terms of home insurance and even housing rental eligibility if DTC canine genetic test usage became more widespread in housing practices. Without significant oversight, highly innacurate predicted breed results can easily result in loss of home or insurance...

It is also important to consider the context of the other services that many DTC genetic tests provide: health predictions. Some services (Embark, Wisdom Panel, and Orivet) provide information about specific risk variants that a dog does or does not carry. The potential for such information to be misunderstood and misapplied has been discussed widely in discussion of the risks of DTC genetic testing broadly (need citations). DNA My Dog and Accu-Metrics, on the other hand, provide general information about health risks based on the breeds detected. Darwin's Ark, in contrast, has decided not to provide health predictions because of a lack of rigorous standards for these estimations \[[10]\]. Because consumers are likely to be interested in DTC health testing, this position raises interesting questions about what the ethical burden is for non-human DTC genetic testing.

Certainly, despite being priced similarly to human DTC test kits, DTC canine genetic testing is not held to the same regulatory standards as human testing, at least in the United States. The human DTC market underwent a major shift in the mid-2010s when the FDA began regulating the health results they are allowed to provide to consumers \[CITE FDA NOTICE/ARTICLE\]. Anecdotes of similar tragic misinterpretations of genetic risk can also be found in the canine DTC space (e.g., \[cite\], co-authored by some of the developers of Darwin's Ark's test). Here, we clearly demonstrate that ancestry predictions can differ widely among services. Therefore, the extent to which health predictions differ among tests would also be an interesting question for future studies of the industry.

Additionally, the lack of regulation also presents ample opportunity for misinformation, even if unintentional. This study demonstrates that Accu-Metrics breed predictions are heavily influenced by the user-provided photograph; there was, in fact, no evidence that the results were influenced by the DNA. In fact, this test identified the registered breed less often than NASNet, the image prediction model, and a human genetic test produced by the same company reportedly assigned First Nations ancestry to canine DNA samples \[[28]\]. Despite these issues, this product has been promoted by companies such as the pet pharmacy PetMeds \[[29]\]. Without DTC test industry regulation, it is difficult to determine how such errors arise, but the present study suggests they are frequent. Therefore, this systematic comparison of DTC genetic tests for dogs suggests that it is imperative that consumers approach the results of these tests with care. In some cases, a photograph can change everything.

## References

[]{#ref-5LNIDiUt .anchor}1. **The use of molecular genetics in the improvement of agricultural populations** Jack CM Dekkers, Frédéric Hospital *Nature Reviews Genetics* (2002-01) <https://doi.org/bsq7pk> DOI: [10.1038/nrg701] · PMID: [11823788]

[]{#ref-6GtbXGFE .anchor}2. **Animal Genetics Market revenue to cross USD 6.4 Bn by 2027: Global Market Insights, Inc.** Global Market Insights Inc *GlobeNewswire News Room* (2021-03-08) <https://www.globenewswire.com/news-release/2021/03/08/2188474/0/en/Animal-Genetics-Market-revenue-to-cross-USD-6-4-Bn-by-2027-Global-Market-Insights-Inc.html>

[]{#ref-YhSywT2b .anchor}3. **Researcher responsibilities and genetic counseling for pure-bred dog populations** Jerold S Bell *The Veterinary Journal* (2011-08) <https://doi.org/dr4ht3> DOI: [10.1016/j.tvjl.2011.06.025] · PMID: [21737320]

[]{#ref-7iOBBKO6 .anchor}4. **Genetic testing in domestic cats** Leslie A Lyons *Molecular and Cellular Probes* (2012-12) <https://doi.org/f4gjgw> DOI: [10.1016/j.mcp.2012.04.004] · PMID: [22546621] · PMCID: [PMC3541004]

[]{#ref-ykgRyoc9 .anchor}5. **Best Dog DNA Tests 2023: DNA My Dog vs Wisdom Panel vs Embark vs Orivet vs EasyDNA & More** Sally Jones *Canine Journal* (2016-10-21) <https://www.caninejournal.com/dog-dna-tests-reviews/>

[]{#ref-oM4FJK9x .anchor}6. **How pet DNA tests work \| The science behind Wisdom Panel™ tests** Wisdom Panel™ <https://www.wisdompanel.com/en-us/our-science>

[]{#ref-fTvai3X7 .anchor}7. **Wisdom Panel™ \| The world\'s most accurate pet DNA test service** Wisdom Panel™ <https://www.wisdompanel.com/en-us>

[]{#ref-10tVMdVL0 .anchor}8. **Geno Pet Dog Breed Identification Test - DNA Test - Orivet** <https://www.orivet.com/store/canine-mixed-breed-screen/geno-pet-dog-breed-identification-test>

[]{#ref-MjfoazN4 .anchor}9. **Pedigree Breed Products - DNA Test - Orivet** <https://www.orivet.com/store/breed-list>

[]{#ref-wGErpuWM .anchor}10. **FAQs -- Darwin\'s Ark** <https://darwinsark.org/faqs/>

[]{#ref-13HrevujZ .anchor}11. **Inferring genome-wide patterns of admixture in Qataris using fifty-five ancestral populations** Larsson Omberg, Jacqueline Salit, Neil Hackett, Jennifer Fuller, Rebecca Matthew, Lotfi Chouchane, Juan L Rodriguez-Flores, Carlos Bustamante, Ronald G Crystal, Jason G Mezey *BMC Genetics* (2012) <https://doi.org/gb3dhr> DOI: [10.1186/1471-2156-13-49] · PMID: [22734698] · PMCID: [PMC3512499]

[]{#ref-yx4y88bd .anchor}12. **Help Centre and Canine FAQ \| DNA My Dog** <https://dnamydog.com/help/help-centre/>

[]{#ref-g0Gn4HKM .anchor}13. **Dog Breed Identification - Identify the Breeds in a Mixed-Breed Dog** accu-metrics *accu-metrics.com* <https://www.via-pet.com/canine-testing/p/dog-breed-identification>

[]{#ref-Sm2UTroe .anchor}14. **r/DoggyDNA** reddit <https://www.reddit.com/r/DoggyDNA/>

[]{#ref-m8z5QW6p .anchor}15. **Genomic Analyses Reveal the Influence of Geographic Origin, Migration, and Hybridization on Modern Dog Breed Development** Heidi G Parker, Dayna L Dreger, Maud Rimbault, Brian W Davis, Alexandra B Mullen, Gretchen Carpintero-Ramirez, Elaine A Ostrander *Cell Reports* (2017-04) <https://doi.org/gfpn24> DOI: [10.1016/j.celrep.2017.03.079] · PMID: [28445722] · PMCID: [PMC5492993]

[]{#ref-5i3L8xiJ .anchor}16. **Knowing Your Dog Breed: Identifying a Dog Breed with Deep Learning** Punyanuch Borwarnginn, Worapan Kusakunniran, Sarattha Karnjanapreechakorn, Kittikhun Thongkanchorn *International Journal of Automation and Computing* (2020-11-13) <https://doi.org/grwfjc> DOI: [10.1007/s11633-020-1261-0]

[]{#ref-qtriCJLm .anchor}17. **Dog Breed Identification Using Deep Learning** Zalan Raduly, Csaba Sulyok, Zsolt Vadaszi, Attila Zolde *2018 IEEE 16th International Symposium on Intelligent Systems and Informatics (SISY)* (2018-09) <https://doi.org/grwfjg> DOI: [10.1109/sisy.2018.8524715]

[]{#ref-1C5P7Vjxt .anchor}18. **Breakthrough Conventional Based Approach for Dog Breed Classification Using CNN with Transfer Learning** Punyanuch Borwarnginn, Kittikhun Thongkanchorn, Sarattha Kanchanapreechakorn, Worapan Kusakunniran *2019 11th International Conference on Information Technology and Electrical Engineering (ICITEE)* (2019-10) <https://doi.org/grwfjf> DOI: [10.1109/iciteed.2019.8929955]

[]{#ref-swvBbKnV .anchor}19. **timm: (Unofficial) PyTorch Image Models** Ross Wightman <https://github.com/rwightman/pytorch-image-models>

[]{#ref-Rb9MbDag .anchor}20. **Small Sample Confidence Intervals for the Odds Ratio** Raef Lawson *Communications in Statistics - Simulation and Computation* (2004-10) <https://doi.org/fsc7pw> DOI: [10.1081/sac-200040691]

[]{#ref-PjIUHjUS .anchor}21. **Zero‐cell corrections in random‐effects meta‐analyses** Frank Weber, Guido Knapp, Katja Ickstadt, Günther Kundt, Änne Glass *Research Synthesis Methods* (2020-10-21) <https://doi.org/grwfjb> DOI: [10.1002/jrsm.1460] · PMID: [32991790]

[]{#ref-12Pi2iOc6 .anchor}22. **The Problem of Zero Cells in the Analysis of Contingency Tables** Justyna Brzezińska *Zeszyty Naukowe Uniwersytetu Ekonomicznego w Krakowie* (2015) <https://doi.org/grwfjh> DOI: [10.15678/znuek.2015.0941.0504]

[]{#ref-bHJOW3c3 .anchor}23. **vcd: Visualizing Categorical Data** David Meyer \[aut, cre, Achim Zeileis, Kurt Hornik, Florian Gerber, Michael Friendly (2023-02-01) <https://CRAN.R-project.org/package=vcd>

[]{#ref-14R0uPPU0 .anchor}24. **Ternary: Create Ternary and Holdridge Plots** Martin R Smith, Lilian Sanselme (2023-02-20) <https://CRAN.R-project.org/package=Ternary>

[]{#ref-iU6qp1ua .anchor}25. **Dog DNA Test - Orivet** <https://www.orivet.com/store/canine-full-breed-profile>

[]{#ref-dlL0wgnz .anchor}26. **Stanford Dogs dataset for Fine-Grained Visual Categorization** <http://vision.stanford.edu/aditya86/ImageNetDogs/>

[]{#ref-bG83ce1y .anchor}27. **Dog Breeds Banned By Home Insurance Companies -- Forbes Advisor** <https://www.forbes.com/advisor/homeowners-insurance/banned-dog-breed-lists/>

[]{#ref-AvCapF7F .anchor}28. **A Sketchy DNA Testing Service Said Dogs Had First Nations Ancestry** Sarah Emerson *Vice* (2018-06-14) <https://www.vice.com/en/article/435pnp/a-sketchy-dna-testing-service-said-dogs-had-first-nations-ancestry-viaguard>

[]{#ref-12tXxAusw .anchor}29. **\[New Product\] Viaguard DNAffirm Canine DNA Testing Kit** 1-800-PetMeds *PetMeds® Pet Health Blog* (2017-09-11) <https://blog.petmeds.com/pet-supplies-products/viaguard-dnaffirm-canine-dna-testing-kit/>

  [1]: #ref-5LNIDiUt
  [2]: #ref-6GtbXGFE
  [3]: #ref-YhSywT2b
  [4]: #ref-7iOBBKO6
  [5]: #ref-ykgRyoc9
  [6]: #ref-oM4FJK9x
  [7]: #ref-fTvai3X7
  [8]: #ref-10tVMdVL0
  [9]: #ref-MjfoazN4
  [10]: #ref-wGErpuWM
  [11]: #ref-13HrevujZ
  [12]: #ref-yx4y88bd
  [13]: #ref-g0Gn4HKM
  [14]: #ref-Sm2UTroe
  [15]: #ref-m8z5QW6p
  [16]: #ref-5i3L8xiJ
  [17]: #ref-qtriCJLm
  [18]: #ref-1C5P7Vjxt
  [19]: #ref-swvBbKnV
  [20]: #ref-Rb9MbDag
  [21]: #ref-PjIUHjUS
  [22]: #ref-12Pi2iOc6
  [23]: #ref-bHJOW3c3
  [24]: #ref-14R0uPPU0
  [25]: #tbl:subjects
  [26]: #fig:pies
  [25]: #ref-iU6qp1ua
  [27]: #tbl:accuracy
  [Figure 1: Breed ancestry predictions from six DTC dog genetic testing companies as well as a pretrained image classifier.]: media/image1.png {width="6.5in" height="10.291666666666666in"}
  [26]: #ref-dlL0wgnz
  [28]: #fig:tern
  [Figure 2: Ternary plots identifying the breed clades of results predicted by each test. Each dog is represented by a circle in blue (control) or red (treatment). The position of the circle relative to the three axes indicates the percentage of results belonging to the breed clade of the DNA donor, photographed dog, or other clades. A result that is 100% concordant with the DNA donor's registered breed will be placed at the apex of the triangle. A result that is 100% concordant with the photographed dog's breed (in the treatment condition only) will be located at the top left. Offset from these positions can be interpreted by looking at the position relative to the other two vertices on a 0 to 100 scale. Darker colors indicate multiple circles mapping to the same position.]: media/image2.png {width="6.5in" height="3.648786089238845in"}
  [27]: #ref-bG83ce1y
  [28]: #ref-AvCapF7F
  [29]: #ref-12tXxAusw
  [10.1038/nrg701]: https://doi.org/10.1038/nrg701
  [11823788]: https://www.ncbi.nlm.nih.gov/pubmed/11823788
  [10.1016/j.tvjl.2011.06.025]: https://doi.org/10.1016/j.tvjl.2011.06.025
  [21737320]: https://www.ncbi.nlm.nih.gov/pubmed/21737320
  [10.1016/j.mcp.2012.04.004]: https://doi.org/10.1016/j.mcp.2012.04.004
  [22546621]: https://www.ncbi.nlm.nih.gov/pubmed/22546621
  [PMC3541004]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3541004
  [10.1186/1471-2156-13-49]: https://doi.org/10.1186/1471-2156-13-49
  [22734698]: https://www.ncbi.nlm.nih.gov/pubmed/22734698
  [PMC3512499]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3512499
  [10.1016/j.celrep.2017.03.079]: https://doi.org/10.1016/j.celrep.2017.03.079
  [28445722]: https://www.ncbi.nlm.nih.gov/pubmed/28445722
  [PMC5492993]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5492993
  [10.1007/s11633-020-1261-0]: https://doi.org/10.1007/s11633-020-1261-0
  [10.1109/sisy.2018.8524715]: https://doi.org/10.1109/sisy.2018.8524715
  [10.1109/iciteed.2019.8929955]: https://doi.org/10.1109/iciteed.2019.8929955
  [10.1081/sac-200040691]: https://doi.org/10.1081/sac-200040691
  [10.1002/jrsm.1460]: https://doi.org/10.1002/jrsm.1460
  [32991790]: https://www.ncbi.nlm.nih.gov/pubmed/32991790
  [10.15678/znuek.2015.0941.0504]: https://doi.org/10.15678/znuek.2015.0941.0504
