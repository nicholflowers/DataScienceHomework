

```python
import pandas as pd 
import numpy as np
```


```python
#map to purchase data file
purchase_data =pd.read_csv("purchase_data.json")
```


```python
#read data from json file?
game_df = pd.read_json("purchase_data.json")
game_df.head(50)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Sally64</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
    </tr>
    <tr>
      <th>13</th>
      <td>23</td>
      <td>Male</td>
      <td>77</td>
      <td>Piety, Guardian of Riddles</td>
      <td>3.68</td>
      <td>Seorithstilis90</td>
    </tr>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
    </tr>
    <tr>
      <th>15</th>
      <td>21</td>
      <td>Male</td>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>4.77</td>
      <td>Haellysu29</td>
    </tr>
    <tr>
      <th>16</th>
      <td>22</td>
      <td>Female</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>1.14</td>
      <td>Sundista85</td>
    </tr>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
    </tr>
    <tr>
      <th>20</th>
      <td>24</td>
      <td>Male</td>
      <td>78</td>
      <td>Glimmer, Ender of the Moon</td>
      <td>2.33</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
    </tr>
    <tr>
      <th>23</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Chanosia65</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Idai61</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
    </tr>
    <tr>
      <th>30</th>
      <td>21</td>
      <td>Female</td>
      <td>155</td>
      <td>War-Forged Gold Deflector</td>
      <td>3.73</td>
      <td>Eulaeria40</td>
    </tr>
    <tr>
      <th>31</th>
      <td>18</td>
      <td>Male</td>
      <td>37</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>1.93</td>
      <td>Iarilis73</td>
    </tr>
    <tr>
      <th>32</th>
      <td>19</td>
      <td>Male</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Malunil62</td>
    </tr>
    <tr>
      <th>33</th>
      <td>24</td>
      <td>Male</td>
      <td>90</td>
      <td>Betrayer</td>
      <td>1.67</td>
      <td>Iskimnya76</td>
    </tr>
    <tr>
      <th>34</th>
      <td>22</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Yararmol43</td>
    </tr>
    <tr>
      <th>35</th>
      <td>21</td>
      <td>Female</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Aisur51</td>
    </tr>
    <tr>
      <th>36</th>
      <td>20</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Undare39</td>
    </tr>
    <tr>
      <th>37</th>
      <td>31</td>
      <td>Male</td>
      <td>171</td>
      <td>Scalpel</td>
      <td>3.62</td>
      <td>Sondossa91</td>
    </tr>
    <tr>
      <th>38</th>
      <td>20</td>
      <td>Male</td>
      <td>25</td>
      <td>Hero Cane</td>
      <td>1.03</td>
      <td>Chamjasknya65</td>
    </tr>
    <tr>
      <th>39</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Lassilsa63</td>
    </tr>
    <tr>
      <th>40</th>
      <td>32</td>
      <td>Male</td>
      <td>7</td>
      <td>Thorn, Satchel of Dark Souls</td>
      <td>4.51</td>
      <td>Tyisur83</td>
    </tr>
    <tr>
      <th>41</th>
      <td>19</td>
      <td>Female</td>
      <td>124</td>
      <td>Venom Claymore</td>
      <td>2.72</td>
      <td>Aeral43</td>
    </tr>
    <tr>
      <th>42</th>
      <td>24</td>
      <td>Male</td>
      <td>25</td>
      <td>Hero Cane</td>
      <td>1.03</td>
      <td>Lassadarsda57</td>
    </tr>
    <tr>
      <th>43</th>
      <td>22</td>
      <td>Male</td>
      <td>68</td>
      <td>Storm-Weaver, Slayer of Inception</td>
      <td>2.49</td>
      <td>Alaephos75</td>
    </tr>
    <tr>
      <th>44</th>
      <td>22</td>
      <td>Male</td>
      <td>85</td>
      <td>Malificent Bag</td>
      <td>2.17</td>
      <td>Frichjask31</td>
    </tr>
    <tr>
      <th>45</th>
      <td>20</td>
      <td>Male</td>
      <td>120</td>
      <td>Agatha</td>
      <td>1.91</td>
      <td>Eusur90</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Male</td>
      <td>17</td>
      <td>Lazarus, Terror of the Earth</td>
      <td>3.47</td>
      <td>Palatyon26</td>
    </tr>
    <tr>
      <th>47</th>
      <td>24</td>
      <td>Male</td>
      <td>141</td>
      <td>Persuasion</td>
      <td>3.27</td>
      <td>Saellyra72</td>
    </tr>
    <tr>
      <th>48</th>
      <td>20</td>
      <td>Male</td>
      <td>73</td>
      <td>Ritual Mace</td>
      <td>3.74</td>
      <td>Ililsa62</td>
    </tr>
    <tr>
      <th>49</th>
      <td>22</td>
      <td>Male</td>
      <td>151</td>
      <td>Severance</td>
      <td>1.85</td>
      <td>Eosur70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate player count
player_count = len(game_df["SN"].unique())
players_df = pd.DataFrame([{"Total Players": player_count}])
players_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis


```python
# # # create dataframe for player count
# # totalplayers_df =pd.DataFrame([{'Total Players':'player_count'}])
# # totalplayers_df.head()

# # Number of Unique Items
# uniqueitems =game_df ["Item Name"].nunique()       
# uniqueitems

# #Purchasing Analysis (Total) - Average Purchase Price
# Priceaverage= game_df['Price'].mean()
# Priceaverage

# #Total Number of Purchases
# Purch_Count =game_df['Price'].count()
# Purch_Count

# #Purchasing Analysis (total) - Total Revenue

# Total_Rev =game_df['Price'].sum()
# Total_Rev

```


```python
#Purchasing Analysis (Total) - Number of Unique Items

# Number of Unique Items
uniqueitems =game_df ["Item ID"].nunique()
uniqueitems
```




    183




```python
#Purchasing Analysis (Total) - Average Purchase Price
Priceaverage= game_df['Price'].mean()
Priceaverage
```




    2.931192307692303




```python
#Purchasing Analysis (total) - Total Number of Purchases

Purch_Count =game_df['Price'].count()
Purch_Count
```




    780




```python
#Purchasing Analysis (total) - Total Revenue

Total_Rev =round(game_df['Price'].sum(),2)

Total_Rev
```




    2286.33



# Gender Demographics


```python
#creates df of unique player names by only keeping the last occurence
no_dup_players = game_df.drop_duplicates(['SN'], keep ='last')

#counts gender values from the df with no duplicate screen names
gender_counts = no_dup_players['Gender'].value_counts().reset_index()

#adds column for % of players using player count from first table and gender_count 
#column which is a count from line above
gender_counts['% of Players'] = gender_counts['Gender']/player_count * 100

#renames columns
gender_counts.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)

#sets index as Gender for aesthetics 
gender_counts.set_index(['Gender'], inplace = True)

#just checking percents sum to 100%
gender_counts['% of Players'].sum()

#formats table
gender_counts.style.format({"% of Players": "{:.1f}%"})
```




<style  type="text/css" >
</style>  
<table id="T_631856ae_1b5c_11e8_81c8_38c98623293a" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Players</th> 
        <th class="col_heading level0 col1" >% of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_631856ae_1b5c_11e8_81c8_38c98623293alevel0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow0_col0" class="data row0 col0" >465</td> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow0_col1" class="data row0 col1" >81.2%</td> 
    </tr>    <tr> 
        <th id="T_631856ae_1b5c_11e8_81c8_38c98623293alevel0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow1_col0" class="data row1 col0" >100</td> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow1_col1" class="data row1 col1" >17.5%</td> 
    </tr>    <tr> 
        <th id="T_631856ae_1b5c_11e8_81c8_38c98623293alevel0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow2_col0" class="data row2 col0" >8</td> 
        <td id="T_631856ae_1b5c_11e8_81c8_38c98623293arow2_col1" class="data row2 col1" >1.4%</td> 
    </tr></tbody> 
</table> 



# Purchasing Analysis by Gender


```python
# 
# #counts purchases by gender
# purch_by_gen = (game_df.groupby('Gender')['Gender'].count())
# #game_df= game_df['Gender'].value_counts().reset_index()
# #df.columns = ['Gender', 'count']
# purch_by_gen

# # sums price by gender
# total_purch_by_gen = pd.DataFrame(purchase_data.groupby('Gender')['Price'].sum())

# #merges the two data frames from above
# purch_analysis_gen = pd.merge(purch_by_gen, total_pur_by_gen, left_index = True, right_index = True)

# #renames columns
# purch_analysis_gen.rename(columns = {'Gender': '# of Purchases', 'Price':'Total Purchase Value'}, inplace=True)

# #adds column for average purchase price by gender by dividing total purcahse value by gender by # of purchases by gender
# purch_analysis_gen['Average Purchase Price'] = purch_analysis_gen['Total Purchase Value']/purch_analysis_gen['# of Purchases']

# #merges gender counts from above table (excluding dup SNs) into current df 
# purch_analysis_gen = purch_analysis_gen.merge(gender_counts, left_index = True, right_index = True)

# # calculates and adds normalized total column by dividing total purchase value by unique # of players by genger
# purch_analysis_gen['Normalized Totals'] = purch_analysis_gen['Total Purchase Value']/purch_analysis_gen['# of Players']
# purch_analysis_gen

# #deletes columns not needed for table (# of Players was used for normalized totals while % of players came from gender count table)
# del purch_analysis_gen['% of Players']
# del purch_analysis_gen['# of Players']

# #resets index for aesthetics 
# #purch_analysis_gen.set_index('Gender', inplace=True)

# #formats table
# purch_analysis_gen.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-10-507acb26f750> in <module>()
          7 
          8 # sums price by gender
    ----> 9 total_purch_by_gen = pd.DataFrame(purchase_data.groupby('Gender')['Price'].sum())
         10 
         11 #merges the two data frames from above


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in groupby(self, by, axis, level, as_index, sort, group_keys, squeeze, **kwargs)
       4414         return groupby(self, by=by, axis=axis, level=level, as_index=as_index,
       4415                        sort=sort, group_keys=group_keys, squeeze=squeeze,
    -> 4416                        **kwargs)
       4417 
       4418     def asfreq(self, freq, method=None, how=None, normalize=False,


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in groupby(obj, by, **kwds)
       1697         raise TypeError('invalid type: %s' % type(obj))
       1698 
    -> 1699     return klass(obj, by, **kwds)
       1700 
       1701 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in __init__(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, squeeze, **kwargs)
        390                                                     level=level,
        391                                                     sort=sort,
    --> 392                                                     mutated=self.mutated)
        393 
        394         self.obj = obj


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in _get_grouper(obj, key, axis, level, sort, mutated)
       2688                 in_axis, name, level, gpr = False, None, gpr, None
       2689             else:
    -> 2690                 raise KeyError(gpr)
       2691         elif isinstance(gpr, Grouper) and gpr.key is not None:
       2692             # Add key to exclusions


    KeyError: 'Gender'



```python
#purchases by gender
purchcount_by_gen = pd.DataFrame(game_df.groupby('Gender')['Gender'].count())
purchcount_by_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#price sums by gender
total_purch_by_gen = pd.DataFrame(game_df.groupby('Gender')['Price'].sum())
total_purch_by_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merges previous 2 dataframes 

purch_analysis_gen = pd.merge(purchcount_by_gen, total_purch_by_gen, left_index = True, right_index = True)
purch_analysis_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#renames columns
purch_analysis_gen.rename(columns = {'Gender': 'Purchases', 'Price':'Purchase Total'}, inplace=True)
purch_analysis_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Purchase Total</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#add column for average purchase price 
purch_analysis_gen['Average Purchase Price'] = purch_analysis_gen['Purchase Total']/purch_analysis_gen['Purchases']
purch_analysis_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Purchase Total</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
# calculates and adds normalized total column by dividing total purchase value by unique # of players by genger
purch_analysis_gen['Normalized Totals'] = purch_analysis_gen['Purchase Total']/purch_analysis_gen['Purchases']
purch_analysis_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Purchase Total</th>
      <th>Average Purchase Price</th>
      <th>Gender</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>136</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>633</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>11</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
#deletes columns not needed for table (# of Players was used for normalized totals while % of players came from gender count table)
del purch_analysis_gen['Gender']
purch_analysis_gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Total</th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>382.91</td>
      <td>2.815515</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>35.74</td>
      <td>3.249091</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
#formats table
purch_analysis_gen.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_81e33a86_1c03_11e8_a98d_38c98623293a" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Total</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_81e33a86_1c03_11e8_a98d_38c98623293alevel0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow0_col0" class="data row0 col0" >382.91</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow0_col1" class="data row0 col1" >$2.82</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow0_col2" class="data row0 col2" >$2.82</td> 
    </tr>    <tr> 
        <th id="T_81e33a86_1c03_11e8_a98d_38c98623293alevel0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow1_col0" class="data row1 col0" >1867.68</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow1_col1" class="data row1 col1" >$2.95</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow1_col2" class="data row1 col2" >$2.95</td> 
    </tr>    <tr> 
        <th id="T_81e33a86_1c03_11e8_a98d_38c98623293alevel0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow2_col0" class="data row2 col0" >35.74</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow2_col1" class="data row2 col1" >$3.25</td> 
        <td id="T_81e33a86_1c03_11e8_a98d_38c98623293arow2_col2" class="data row2 col2" >$3.25</td> 
    </tr></tbody> 
</table> 



# Age Demographics


```python
# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals
```


```python
#creates a column 'age_bin' based on age range
game_df.loc[(game_df['Age'] < 10), 'age_bin'] = "< 10"
game_df.loc[(game_df['Age'] >= 10) & (game_df['Age'] <= 14), 'age_bin'] = "10 - 14"
game_df.loc[(game_df['Age'] >= 15) & (game_df['Age'] <= 19), 'age_bin'] = "15 - 19"
game_df.loc[(game_df['Age'] >= 20) & (game_df['Age'] <= 24), 'age_bin'] = "20 - 24"
game_df.loc[(game_df['Age'] >= 25) & (game_df['Age'] <= 29), 'age_bin'] = "25 - 29"
game_df.loc[(game_df['Age'] >= 30) & (game_df['Age'] <= 34), 'age_bin'] = "30 - 34"
game_df.loc[(game_df['Age'] >= 35) & (game_df['Age'] <= 39), 'age_bin'] = "35 - 39"
game_df.loc[(game_df['Age'] >= 40), 'age_bin'] = "> 40"

#double checked count
game_df[['age_bin', 'Age']].count()
```




    age_bin    780
    Age        780
    dtype: int64




```python
# # counts purchases by age bin by counting screen names (non-unique)
# purch_count_age = pd.DataFrame(game_df.groupby('age_bin')['SN'].count())

# #finds avg price of purchases by age bin
# avg_price_age = pd.DataFrame(purchase_data.groupby('age_bin')['Price'].mean())

# #finds total purchase value by age bin
# tot_purch_age = pd.DataFrame(purch_data.groupby('age_bin')['Price'].sum())

# #deletes multiple occurances of SN while only keeping last, then counts # of unique
# #players by age bin
# no_dup_age = pd.DataFrame(pur_data.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())

# #merges all info from above into one df
# merge_age = pd.merge(pur_count_age, avg_price_age, left_index = True, right_index = True).merge(tot_pur_age, left_index = True, right_index = True).merge(no_dup_age, left_index = True, right_index = True)

# #renames columns
# merge_age.rename(columns = {"SN_x": "# of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "# of Purchasers"}, inplace = True)

# #calculates normalized totals
# merge_age['Normalized Totals'] = merge_age['Total Purchase Value']/merge_age['# of Purchasers']

# #rest index for aesthetics
# merge_age.index.rename("Age", inplace = True)

# # formats
# merge_age.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-59-205d9200851c> in <module>()
          3 
          4 #finds avg price of purchases by age bin
    ----> 5 avg_price_age = pd.DataFrame(purchase_data.groupby('age_bin')['Price'].mean())
          6 
          7 #finds total purchase value by age bin


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in groupby(self, by, axis, level, as_index, sort, group_keys, squeeze, **kwargs)
       4414         return groupby(self, by=by, axis=axis, level=level, as_index=as_index,
       4415                        sort=sort, group_keys=group_keys, squeeze=squeeze,
    -> 4416                        **kwargs)
       4417 
       4418     def asfreq(self, freq, method=None, how=None, normalize=False,


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in groupby(obj, by, **kwds)
       1697         raise TypeError('invalid type: %s' % type(obj))
       1698 
    -> 1699     return klass(obj, by, **kwds)
       1700 
       1701 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in __init__(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, squeeze, **kwargs)
        390                                                     level=level,
        391                                                     sort=sort,
    --> 392                                                     mutated=self.mutated)
        393 
        394         self.obj = obj


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in _get_grouper(obj, key, axis, level, sort, mutated)
       2688                 in_axis, name, level, gpr = False, None, gpr, None
       2689             else:
    -> 2690                 raise KeyError(gpr)
       2691         elif isinstance(gpr, Grouper) and gpr.key is not None:
       2692             # Add key to exclusions


    KeyError: 'age_bin'



```python
# counts purchases by age bin by counting screen names (non-unique)
purch_count_age = pd.DataFrame(game_df.groupby('age_bin')['SN'].count())
purch_count_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
#finds avg purchase price 
avg_price_age = pd.DataFrame(game_df.groupby('age_bin')['Price'].mean())
avg_price_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>2.770000</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>2.905414</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>2.913006</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>2.962640</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>3.082031</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>2.842857</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>2.980714</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>3.161765</td>
    </tr>
  </tbody>
</table>
</div>




```python
#finds total purchase value by age bin
tot_purch_age = pd.DataFrame(game_df.groupby('age_bin')['Price'].sum())
tot_purch_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>96.95</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>386.42</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>978.77</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>370.33</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>197.25</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>119.40</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>83.46</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>53.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
#deletes duplicate SN, then counts # of unique
#players by age bin
no_dup_age = pd.DataFrame(game_df.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())
no_dup_age


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge all info from above into one df
merge_age = pd.merge(purch_count_age, avg_price_age, left_index = True, right_index = True).merge(tot_purch_age, left_index = True, right_index = True).merge(no_dup_age, left_index = True, right_index = True)
merge_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN_x</th>
      <th>Price_x</th>
      <th>Price_y</th>
      <th>SN_y</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#rename columns
merge_age.rename(columns = {"SN_x": "# of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "# of Purchasers"}, inplace = True)
merge_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th># of Purchasers</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculates normalized totals
normalized_totals = merge_age['Normalized Totals'] = merge_age['Total Purchase Value']/merge_age['# of Purchasers']
normalized_totals
```




    age_bin
    10 - 14    4.215217
    15 - 19    3.864200
    20 - 24    3.779035
    25 - 29    4.256667
    30 - 34    4.196809
    35 - 39    4.422222
    < 10       4.392632
    > 40       4.886364
    dtype: float64




```python
#reset index 
index_reset = merge_age.index.rename("Age", inplace = True)
index_reset
```


```python
# formatting
reformat = merge_age.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})
reformat

```




<style  type="text/css" >
</style>  
<table id="T_1d730902_1c09_11e8_93c3_38c98623293a" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Purchases</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" ># of Purchasers</th> 
        <th class="col_heading level0 col4" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row0" class="row_heading level0 row0" >10 - 14</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow0_col0" class="data row0 col0" >35</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow0_col1" class="data row0 col1" >$2.77</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow0_col2" class="data row0 col2" >$96.95</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow0_col3" class="data row0 col3" >23</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow0_col4" class="data row0 col4" >$4.22</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row1" class="row_heading level0 row1" >15 - 19</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow1_col0" class="data row1 col0" >133</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow1_col1" class="data row1 col1" >$2.91</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow1_col2" class="data row1 col2" >$386.42</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow1_col3" class="data row1 col3" >100</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow1_col4" class="data row1 col4" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row2" class="row_heading level0 row2" >20 - 24</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow2_col0" class="data row2 col0" >336</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow2_col1" class="data row2 col1" >$2.91</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow2_col2" class="data row2 col2" >$978.77</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow2_col3" class="data row2 col3" >259</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow2_col4" class="data row2 col4" >$3.78</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row3" class="row_heading level0 row3" >25 - 29</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow3_col0" class="data row3 col0" >125</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow3_col1" class="data row3 col1" >$2.96</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow3_col2" class="data row3 col2" >$370.33</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow3_col3" class="data row3 col3" >87</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow3_col4" class="data row3 col4" >$4.26</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row4" class="row_heading level0 row4" >30 - 34</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow4_col0" class="data row4 col0" >64</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow4_col1" class="data row4 col1" >$3.08</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow4_col2" class="data row4 col2" >$197.25</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow4_col3" class="data row4 col3" >47</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow4_col4" class="data row4 col4" >$4.20</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row5" class="row_heading level0 row5" >35 - 39</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow5_col0" class="data row5 col0" >42</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow5_col1" class="data row5 col1" >$2.84</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow5_col2" class="data row5 col2" >$119.40</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow5_col3" class="data row5 col3" >27</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow5_col4" class="data row5 col4" >$4.42</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row6" class="row_heading level0 row6" >< 10</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow6_col0" class="data row6 col0" >28</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow6_col1" class="data row6 col1" >$2.98</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow6_col2" class="data row6 col2" >$83.46</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow6_col3" class="data row6 col3" >19</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow6_col4" class="data row6 col4" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1d730902_1c09_11e8_93c3_38c98623293alevel0_row7" class="row_heading level0 row7" >> 40</th> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow7_col0" class="data row7 col0" >17</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow7_col1" class="data row7 col1" >$3.16</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow7_col2" class="data row7 col2" >$53.75</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow7_col3" class="data row7 col3" >11</td> 
        <td id="T_1d730902_1c09_11e8_93c3_38c98623293arow7_col4" class="data row7 col4" >$4.89</td> 
    </tr></tbody> 
</table> 




```python
#Top Spenders
#Group by screen name to find total purchase per person, number of purchases per person, and average price price per person
purchase_amt_by_SN = pd.DataFrame(game_df.groupby('SN')['Price'].sum())
num_purchase_by_SN = pd.DataFrame(game_df.groupby('SN')['Price'].count())
avg_purchase_by_SN = pd.DataFrame(game_df.groupby('SN')['Price'].mean())
```


```python
#merge above dataframes
merge_top5 = pd.merge(purchase_amt_by_SN, num_purchase_by_SN, left_index = True, right_index = True).merge(avg_purchase_by_SN, left_index=True, right_index=True)
merge_top5.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price_x</th>
      <th>Price_y</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>6.70</td>
      <td>3</td>
      <td>2.233333</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>5.80</td>
      <td>3</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.27</td>
      <td>1</td>
      <td>1.270000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# rename columns
merge_top5.rename(columns = {'Price_x': 'Total Purchase Value', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)
merge_top5.head()


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>6.70</td>
      <td>3</td>
      <td>2.233333</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>5.80</td>
      <td>3</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.27</td>
      <td>1</td>
      <td>1.270000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# sort highest purchase value to lowest
merge_top5.sort_values('Total Purchase Value', ascending = False, inplace=True)
merge_top5.head()



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# format
merge_top5.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}'})
merge_top5.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items


```python
# gets a count of each item by grouping by Item ID and counting each occurrence
top5_items_ID = pd.DataFrame(game_df.groupby('Item ID')['Item ID'].count())
top5_items_ID.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sort from high to low total purchase count
top5_items_ID.sort_values('Item ID', ascending = False, inplace = True)
top5_items_ID.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#keep the first 6 rows because there is a tie
top5_items_ID = top5_items_ID.iloc[0:6][:]
top5_items_ID
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
    </tr>
    <tr>
      <th>34</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#find the total purchase value of each item
top5_items_total = pd.DataFrame(game_df.groupby('Item ID')['Price'].sum())
top5_items_total.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge purchase count and total purcahse value 
top5_items = pd.merge(top5_items_ID, top5_items_total, left_index = True, right_index = True)
top5_items
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>9</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#drop duplicate items from original dataframe
no_dup_items = game_df.drop_duplicates(['Item ID'], keep = 'last')
no_dup_items.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>age_bin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
      <td>15 - 19</td>
    </tr>
    <tr>
      <th>59</th>
      <td>15</td>
      <td>Male</td>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>Ila44</td>
      <td>15 - 19</td>
    </tr>
    <tr>
      <th>63</th>
      <td>23</td>
      <td>Male</td>
      <td>28</td>
      <td>Flux, Destroyer of Due Diligence</td>
      <td>3.04</td>
      <td>Ryanara76</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>88</th>
      <td>23</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Undotesta33</td>
      <td>20 - 24</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merge to get all other info from the top 6 using the no dup df
top5_merge_ID = pd.merge(top5_items, no_dup_items, left_index = True, right_on = 'Item ID')

top5_merge_ID
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item ID_x</th>
      <th>Price_x</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID_y</th>
      <th>Item Name</th>
      <th>Price_y</th>
      <th>SN</th>
      <th>age_bin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>721</th>
      <td>39</td>
      <td>11</td>
      <td>25.85</td>
      <td>26</td>
      <td>Male</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeduera68</td>
      <td>25 - 29</td>
    </tr>
    <tr>
      <th>766</th>
      <td>84</td>
      <td>11</td>
      <td>24.53</td>
      <td>22</td>
      <td>Female</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Nitherian58</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>772</th>
      <td>31</td>
      <td>9</td>
      <td>18.63</td>
      <td>15</td>
      <td>Male</td>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>Sidap51</td>
      <td>15 - 19</td>
    </tr>
    <tr>
      <th>761</th>
      <td>175</td>
      <td>9</td>
      <td>11.16</td>
      <td>28</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Raeduerin33</td>
      <td>25 - 29</td>
    </tr>
    <tr>
      <th>765</th>
      <td>13</td>
      <td>9</td>
      <td>13.41</td>
      <td>15</td>
      <td>Male</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Aerithnucal56</td>
      <td>15 - 19</td>
    </tr>
    <tr>
      <th>746</th>
      <td>34</td>
      <td>9</td>
      <td>37.26</td>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Ralasti48</td>
      <td>35 - 39</td>
    </tr>
  </tbody>
</table>
</div>




```python
#keep only necessary columns
top5_merge_ID = top5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]
top5_merge_ID

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>721</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>766</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>772</th>
      <td>31</td>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>761</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>765</th>
      <td>13</td>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>746</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#reset index as item ID for aesthetics
top5_merge_ID.set_index(['Item ID'], inplace = True)
top5_merge_ID
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
# rename columns
top5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)
top5_merge_ID
```

    /Users/nicholflowers/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py:2746: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      **kwargs)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#format
top5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_7bce9274_1c0d_11e8_a221_38c98623293a" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row0" class="row_heading level0 row0" >39</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow0_col0" class="data row0 col0" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow0_col1" class="data row0 col1" >11</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow0_col2" class="data row0 col2" >$2.35</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow0_col3" class="data row0 col3" >$25.85</td> 
    </tr>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row1" class="row_heading level0 row1" >84</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow1_col0" class="data row1 col0" >Arcane Gem</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow1_col1" class="data row1 col1" >11</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow1_col2" class="data row1 col2" >$2.23</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow1_col3" class="data row1 col3" >$24.53</td> 
    </tr>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row2" class="row_heading level0 row2" >31</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow2_col0" class="data row2 col0" >Trickster</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow2_col1" class="data row2 col1" >9</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow2_col2" class="data row2 col2" >$2.07</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow2_col3" class="data row2 col3" >$18.63</td> 
    </tr>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row3" class="row_heading level0 row3" >175</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow3_col0" class="data row3 col0" >Woeful Adamantite Claymore</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow3_col1" class="data row3 col1" >9</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow3_col2" class="data row3 col2" >$1.24</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow3_col3" class="data row3 col3" >$11.16</td> 
    </tr>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row4" class="row_heading level0 row4" >13</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow4_col0" class="data row4 col0" >Serenity</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow4_col1" class="data row4 col1" >9</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow4_col2" class="data row4 col2" >$1.49</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow4_col3" class="data row4 col3" >$13.41</td> 
    </tr>    <tr> 
        <th id="T_7bce9274_1c0d_11e8_a221_38c98623293alevel0_row5" class="row_heading level0 row5" >34</th> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow5_col0" class="data row5 col0" >Retribution Axe</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow5_col1" class="data row5 col1" >9</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow5_col2" class="data row5 col2" >$4.14</td> 
        <td id="T_7bce9274_1c0d_11e8_a221_38c98623293arow5_col3" class="data row5 col3" >$37.26</td> 
    </tr></tbody> 
</table> 



# Most Profitable


```python
#find total purchase value and sort by high to low
top5_profit = pd.DataFrame(game_df.groupby('Item ID')['Price'].sum())
top5_profit.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_profit.sort_values('Price', ascending = False, inplace = True)
top5_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
#only keep top 5
top5_profit = top5_profit.iloc[0:5][:]
top5_profit

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
#get item purchase count
pur_count_profit = pd.DataFrame(game_df.groupby('Item ID')['Item ID'].count())
pur_count_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_profit = pd.merge(top5_profit, pur_count_profit, left_index = True, right_index = True, how = 'left')
top5_profit
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Item ID_x</th>
      <th>Item ID_y</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>37.26</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>115</th>
      <td>29.75</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>32</th>
      <td>29.70</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>103</th>
      <td>29.22</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>107</th>
      <td>28.88</td>
      <td>8</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit = pd.merge(top5_profit, no_dup_items, left_index = True, right_on = 'Item ID', how = 'left')
top5_merge_profit
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price_x</th>
      <th>Item ID_x</th>
      <th>Item ID_y</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price_y</th>
      <th>SN</th>
      <th>age_bin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>746</th>
      <td>37.26</td>
      <td>9</td>
      <td>9</td>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Ralasti48</td>
      <td>35 - 39</td>
    </tr>
    <tr>
      <th>705</th>
      <td>29.75</td>
      <td>7</td>
      <td>7</td>
      <td>25</td>
      <td>Male</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Aeral85</td>
      <td>25 - 29</td>
    </tr>
    <tr>
      <th>657</th>
      <td>29.70</td>
      <td>6</td>
      <td>6</td>
      <td>28</td>
      <td>Male</td>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>Tyarithn67</td>
      <td>25 - 29</td>
    </tr>
    <tr>
      <th>716</th>
      <td>29.22</td>
      <td>6</td>
      <td>6</td>
      <td>9</td>
      <td>Male</td>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
      <td>Ilophos58</td>
      <td>&lt; 10</td>
    </tr>
    <tr>
      <th>779</th>
      <td>28.88</td>
      <td>8</td>
      <td>8</td>
      <td>23</td>
      <td>Female</td>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>Alim85</td>
      <td>20 - 24</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit = top5_merge_profit[['Item ID', 'Item Name', 'Item ID_x', 'Price_y','Price_x']]
top5_merge_profit
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>746</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>705</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>657</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>716</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>779</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.set_index(['Item ID'], inplace=True)
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.rename(columns = {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace = True)
top5_merge_profit.head()
```

    /Users/nicholflowers/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py:2746: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      **kwargs)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
top5_merge_profit
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>



# Observations


```python
#1. Males makeup 81% of the game players.

#2. Most purchases were made by people in the 20-24 age group

#3. The total purchase value for the 20-24 age group is $978.77.

```
