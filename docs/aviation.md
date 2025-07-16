# Aviation Project Documentation

##  Constants
The following are constants and approximations made in the model.

## 

| Constant     | Value | Unit |
| ----------- | ----------- |------|
| Days in Year | 365       | - |


| Input     | Value | Unit | Source |
| ----------- | ----------- |------|-----|
| passengers per year | $6 \times10^9$      | $year^{-1}$ | [^1] | 
| seats per aircraft |180 |- |
| flight per aircraft per day  | 2 | $day^{-1}$ | - |


## Equations

Take the estimate of passengers per year to calculate the average number of passengers per day.

$ \text{flights per aircraft per day} = \frac{ \text{passengers per year} }{\text{days per year} } $ 

In order to estimate the required fleet size, we divide the number of passengers per day with the daily capacity of the one aircraft. 

$ \text{required global fleet}  = \frac{ \text{passengers per day} }{ \text{seats per aircraft} \times \text{flights per aircraft per day} }$

## Footnotes 

note that this is number of seats and therefore the true value of passengers flying could be lower. 

[^1]: \text{https://airlinergs.com/cirium-analysis-confirms-2024-as-a-record-breaking-year-in-global-aviation-history/#:~:text=During%202024%2C%20airlines%20offered%20an%20extraordinary%205.85%20billion,5.72%20billion%20seats%20set%20in%202019%20by%202%25.}