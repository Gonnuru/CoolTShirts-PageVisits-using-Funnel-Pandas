# Page Visits Funnel
Cool T-Shirts Inc. I have analyzed data on visits to their website. My job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.
In this case, my funnel is going to describe the following process:
1.	A user visits CoolTShirts.com
2.	A user adds a t-shirt to their cart
3.	A user clicks “checkout”
4.	A user actually purchases a t-shirt

## Data Frame

An insight to the the following dataFrames
- **visits**:  lists all of the users who have visited the website
- **cart**: lists all of the users who have added a t-shirt to their cart
- **checkout**: lists all of the users who have started the checkout
- **purchase**: lists all of the users who have purchased a t-shirt

![]()
![]()

## Funnel Insights
 - On an average the website can see a traffic of around **2000 users**. Registered and unregistered included. 
 - There are around **2052 rows** for the merged dataFrame of ***Visits and Cart***. Of which around **80.5%** of users ended up not placing a T-shirt in their cart
 - Similarily, we have around **602 rows** for the merged dataFrame of ***Cart and Checkout***. Of which percentage of users put items in their cart, but did not proceed to checkout were **20.9%**
 - percentage of users proceeded to checkout, but did not purchase a t-shirt amount to **16.88%**. This insight was gained on merging the dataFrames **Checkout and Purchase** which consisted of **598 rows**
 
### Average Time to Purchase
Using the merged DataFrame, the average time from initial visit to final purchase was around **44 minutes**