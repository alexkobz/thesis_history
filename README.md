Let's consider the use of adjectives and possessive pronouns before the word "democracy" and the results of the word2vec model. Let's start with the speeches of V. Putin and D. Medvedev. The presidents often use the adjectives "Russian" and "our" before democracy, which shows the presidents' focus on domestic development. The words "direct", "parliamentary", "representative", "electronic" indicate that the presidents are concerned with institutional issues. ![](https://github.com/alexkobz/diplom/blob/main/texts/president/president_adj_en.png) \
As for the words used in the same context, none of them catches the eye except the word “statehood.” This confirms what was said at length in the report – the vision of democracy as a “brick” in the “building” of state governance.
| Word | Meaning |
| ----- | -------- |
| Democratic |	0,75 |
| Statehood | 0,53 |
| "Narodovlastie" | 0,50 |
| Civilized | 0,48 |
| Multi-party system | 0,48 |
| Freedom |	0,47 |
| ideology | 0,47 |
| Expression of will | 0,47 |
| Dictatorship | 0,46 |
| World order |	0,46 |

Let us consider the frequency of use of the word “democracy” at meetings of the State Duma.\
![](https://github.com/alexkobz/diplom/blob/main/texts/gosduma/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%83%D0%BF%D0%BE%D0%BC%D0%B8%D0%BD%D0%B0%D0%BD%D0%B8%D0%B8%CC%86%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F%20%D0%93%D0%94.png)\
Over the course of 21 years, members of parliament have used this word quite frequently and regularly. However, there is no clear trend, so the histogram data does not allow us to draw any clear conclusions about whether the relevance of the issues raised has increased or decreased. However, it is clear that the period 2006-2012 stands out against the periods 2000-2005 and 2013-2021. In many ways, the use of democratic vocabulary during this period is, in our opinion, of a “ritual” nature. This is demonstrated, for example, by the surge in use in 2006 at the ceremonial meeting on April 27 on the occasion of the 100th anniversary of the State Duma. The relative frequency of use of adjectives with the word “democracy” is similar to the frequency of use by presidents described above, which is plausible, judging by the high state status. However, the words “Western” and “American” are also presented, which reflects a greater shift towards foreign policy topics.\
![](https://github.com/alexkobz/diplom/blob/main/texts/gosduma/gosduma_adj_en.png)\
Among the words that are close in meaning to the word "democracy", the most interesting are the words "capitalism", "socialism", "bourgeois", "liberalism" and "communism". It is difficult to answer with complete certainty why these words turned out to be close, but we will suggest that perhaps this is connected with the topic of democratic transit and transition period, which is relevant for this period, which is why debates about democracy were often conducted in the space of such concepts from the 20th century as "socialism" and "capitalism".
| Word | Meaning |
| ----- | -------- |
| Dictatorship | 0,67 |
| Democtratic | 0,63 |
| Communism | 0,62 |
| Bourgeois | 0,62 |
| Socialism | 0,62 |
| Democrat | 0,61 |
| Liberalism | 0,61 |
| Capitalism | 0,60 |
| Civilized | 0,60 |
| Conquest | 0,58 |

In the Izvestia newspaper, the word “democracy” is often associated with words related to both institutional development and foreign policy.\
![](https://github.com/alexkobz/diplom/blob/main/texts/izvestia/izvestia_adj_en.png)\
The same can be said, with an adjustment for a small difference in frequency, about such newspapers as Kommersant, Vedomosti, and Nezavisimaya Gazeta.\
![](https://github.com/alexkobz/diplom/blob/main/texts/kommersant/kommersant_adj_en.png)\
![](https://github.com/alexkobz/diplom/blob/main/texts/vedomosti/vedomosti_adj_en.png)\
![](https://github.com/alexkobz/diplom/blob/main/texts/ng/ng_adj_en.png)\
The use of adjectives looks different in the newspaper Vzglyad, on the radio Ekho Moskvy and the newspaper Zavtra.\
![](https://github.com/alexkobz/diplom/blob/main/texts/vzglyad/vzglyad_adj_en.png)\
![](https://github.com/alexkobz/diplom/blob/main/texts/echo/echo_adj_en.png)\
![](https://github.com/alexkobz/diplom/blob/main/texts/zavtra/zavtra_adj_en.png)\
These media outlets predominantly use adjectives such as "Western", "American", "European", which indicates a high proportion of the foreign policy element. Speaking about semantic closeness, for all the media outlets presented, democracy is close to the concepts of different ideologies (liberalism, socialism) and systems (authoritarianism, totalitarianism), which is quite natural. However, two words that are unique to the Vzglyad newspaper cannot help but draw attention: "svetoch" and "globalism". The use of the rare combination "svetoch" and "democracy" indicates a caustic tone of the publications, and the relationship between globalism and democracy reminds us of their mutual negative consequences.
| Word | Meaning |
| ----- | -------- |
| Democratic |	0,67 |
| Liberalism | 0,66 |
| Dictatorship | 0,64 | 
| Beacon of democracy | 0,63 |
| Totalitalism | 0,58 |
| Socialism | 0,56 |
| Freedom | 0,56 | 
| Autocracy | 0,55 | 
| Capitalism | 0,55 |
| Globalism | 0,55 | 

It is also interesting that, based on the results of training the model on transcripts of the radio station “Echo of Moscow”, the words “authoritarianism”, “dictatorship”, “tyranny”, “autocracy” received high weight, which demonstrates the concern of the radio station’s guests about the problems of democracy in the country.
| Word | Meaning |
| ----- | -------- |
| Autoritarism | 0,58 |
| Dictatorship | 0,54 |
| Tyranny | 0,52 |
| Liberalism | 0,52 |
| "Narodovlastie" | 0,52 |
| Democratic | 0,51 | 
| Autocracy | 0,50 |
| Parlamentarism | 0,49 |
| Totalitarism | 0,47 | 
| Sovereign | 0,45 |

In general, over the course of twenty-one years, two major points have been drawn like a red line. The first is democratic transition. The participants in the discussion reflect on the transition from the Soviet system to the new Russian one. The analyzed discourse was a component of the question of ongoing post-Soviet political self-determination, the answer to which for almost all political forces was democracy, although the meaning invested in this concept varied significantly. From this comes the hypothesis of the youth of Russian democracy, which is usually attributed to the imperfections of the political system. This point weakens approximately by the beginning of the second decade, although it continues to be present. The second point is the foreign policy factor. On the contrary, it gains strength throughout the entire period under review and becomes dominant.\
By the end of twenty-one years, the authorities reported satisfactory results of democratization and even the full establishment of democracy in Russia, while the opposition held the opposite point of view. It can also be noted that over time, the discourse was becoming stronger for the "party of power." Other political parties gave in, failing to offer an agenda that would be accepted by the majority of society.
