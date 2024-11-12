# To perform this estimate manually:

## TL;DR (too long... didn't read)
You can estimate roughly with:
```
Total Climate Impact = Total Students × Average Distance × 2 (round trip) × 
                      CO2 per km × Contrails Factor × Other GHG Factor

= 11,700 × 6,750 × 2 × 0.115 × 1.7 × 1.2
```

## Define regions
```
S_r = Total Students × Regional Distribution Percentage

East Coast: S_ec = 11,700 × 0.45 = 5,265 students
Midwest: S_mw = 11,700 × 0.25 = 2,925 students
West Coast: S_wc = 11,700 × 0.20 = 2,340 students
South: S_s = 11,700 × 0.10 = 1,170 students
```

## Round trip distance per-region
```
D_r = One-way distance × 2

East Coast: D_ec = 5,500 × 2 = 11,000 km
Midwest: D_mw = 6,500 × 2 = 13,000 km
West Coast: D_wc = 8,200 × 2 = 16,400 km
South: D_s = 6,800 × 2 = 13,600 km
```

## CO2 Emissions per-region
```
E_r = Number of Students × Round Trip Distance × CO2 per km where CO2 per km = 0.115 kg/km/passenger

East Coast: E_ec = 5,265 × 11,000 × 0.115 = 6,665,175 kg CO2
Midwest: E_mw = 2,925 × 13,000 × 0.115 = 4,367,625 kg CO2
West Coast: E_wc = 2,340 × 16,400 × 0.115 = 4,410,960 kg CO2
South: E_s = 1,170 × 13,600 × 0.115 = 1,831,680 kg CO2
```

## Totals
```
Total CO2 = ∑E_r = E_ec + E_mw + E_wc + E_s
Total CO2 = 17,275,440 kg
```

## Total Climate Impact Including Other Factors
```
CI = Total CO2 × Contrails Factor × Other GHG Factor
where Contrails Factor = 1.7
and Other GHG Factor = 1.2

CI = 17,275,440 × 1.7 × 1.2 = 35,242,898 kg CO2eq
```

## Per-Student Metrics
```
Average CO2 per student = Total CO2 ÷ Total Students
= 17,275,440 ÷ 11,700 = 1,477 kg CO2

Average Climate Impact per student = Total Climate Impact ÷ Total Students
= 35,242,898 ÷ 11,700 = 3,013 kg CO2eq
```
