# NBA Random Walk

<br>
<img src="https://wallpaperaccess.com/full/1305340.jpg" width="250" height="200" />
<br> <br>

## Contents 

* <a href=https://github.com/bryantx22/nba_random_walk#objectives> Defining objectives </a>
* <a href=https://github.com/bryantx22/nba_random_walk/blob/main/README.md#some-initial-numbers> Initial numbers </a>


# Objectives:

1. Update the estimates of Gabel and Redner (https://arxiv.org/pdf/1109.2825.pdf) for the last 8 NBA seasons (2014/15 - 2021/22) and calculate new ones:
    
    - Scoring rate and the composition of scoring plays
    - Probability distribution of time-elapsed between successive scoring events, of the # of lead changes, and of points differentials
    - The anti-persistence parameter 
    - The linear restoring force when teams are leading (probability that the leading team scores again given a lead of size $x$)
    - Characterize the "arcsine law" in the scenario of this asymetric, anti-persistent random walk

<br>

2. To model scoring as an anti-persistence random walk and <strong> compare outcomes against prominent prediction models </strong>

    - With the above parameters and the best fit $\sigma^2$ of the team strength distribution - per Gabel and Redner
    - Assign intrinsic strength for teams and simulate match outcomes; compare results with promiment prediction models listed in Perricone, Shaw and Swieschowicz (http://cs229.stanford.edu/proj2016/report/PerriconeShawSwiechowicz-PredictingResultsforProfessionalBasketballUsingNBAAPIData.pdf)
        - Specifically: for the seasons Perricone, Shaw and Swieschowicz used for validation: use the first half to estimate the relevant parameters (plus assign intrinsic strengths to teams) $\rightarrow$ predict outcomes on the second half 

<br>

3. Other Goals:
 
    - Maintain a rich play-by-play data set for all games played in the seasons under consideration (2014-15 to 2021-22); see pbp_games
    - Understand the evolution of each team's strength over different seasons
    - Construct an interface to investigate the causal impacts of treatments
        - e.g.: Understand the impact of shot selection (small ball; taking more threes) on the probability distribution of lead changes, the distribution of final point spreads, etc.

    - Find funny statistical outliers 


# Some initial numbers

Gabel and Redner investigated all games from 2006/07 to 2009/10. The average scoring rate (scoring plays/sec) they found was 0.03291 and the average point-value per scoring play was 2.0894. In constrast, for the last 8 seasons, while the average scoring rate is aronnd the same at 0.0346, the average point-value per scoring play has risen to <strong> 2.1403 </strong>. This increase can be mostly explained by 3-point-plays acounting for <strong> 24.7% instead of 17% of scoring plays </strong>. It remains to be explained how this phenonmenon impacts other variables of interest, such as the number of lead changes per game. 

As expected, the general characteristics of the game remain the same. For one, The probability distributon of time elapsed between successive scoring events is still appproximately linear on the log scale. The initial uptick can be explained by the change of possession as well as the 24-second shot-clock. 

<image src="https://github.com/bryantx22/nba_random_walk/blob/main/figures/delta_t_prob.png?raw=true" height="400"/>

Likewise, scoring rate remains roughly constant over time, with the same deviations Gabel and Redner noted at the beginning as well as the end of quarters. 

<image src="https://github.com/bryantx22/nba_random_walk/blob/main/figures/scoring_rate.png?raw=true" height="400"/>

Curiously, while the anti-persistence parameter does not differ much from Gabel and Redner's calculation (0.350, +0.002 compared to Gabel and Redner's estimate) <strong> the linear restoring force identified by Gabel and Redner is absent </strong>. Whereas they observed that the probability of the team in the lead scoring again decreases apx. linearly with the size of the lead, the more recent data suggests the opposite, though the growth in probability is rather small. Still, theoretically, <strong> this would make lead changes more sparse and give rise to blow-outs </strong>:

<image src="https://github.com/bryantx22/nba_random_walk/blob/main/figures/restoring_force.png" height="400"/>

<strong> [To be continued...] </strong>