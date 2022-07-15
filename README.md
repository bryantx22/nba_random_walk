### NBA Random Walk

---

Goals:

1. Update the estimates of Gabel and Redner (https://arxiv.org/pdf/1109.2825.pdf) for the last 8 NBA seasons, which include the following variables:
    
    - Scoring rate 
    - Probability distribution of time-elapsed between successive scoring events
    - The anti-persistence parameter 
    - etc.

<br>

2. To model scoring as an anti-persistence random walk and <strong> compare outcomes against prominent prediction models </strong>

    - With the above parameters and the best fit $\sigma^2$ of the team strength distribution - per Gabel and Redner
    - Assign intrinsic strength for teams and simulate match outcomes; compare results with promiment prediction models listed in Perricone, Shaw and Swieschowicz (http://cs229.stanford.edu/proj2016/report/PerriconeShawSwiechowicz-PredictingResultsforProfessionalBasketballUsingNBAAPIData.pdf).

<br>

3. Other goals
 
    - Maintain a rich play-by-play data set for all games played in the seasons under consideration (2014-15 to 2021-22); see pbp_games

    - Understand the impact of shot selection (small ball; taking more threes) on the probability distribution of lead changes, the distribution of final point spreads, etc.

    - Find funny statistical outliers 
    