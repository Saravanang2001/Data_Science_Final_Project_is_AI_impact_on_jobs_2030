import matplotlib.pyplot as pls

def line_plot(psa):

    # Sort using the CORRECT column name
    df = psa.sort_values(by='Automation_Probability_2030')

    pls.figure(figsize=(20, 15))
    pls.plot(
        df['Job_Title'],
        df['Automation_Probability_2030'],
        marker='x',
        linestyle='--',
        color='red'
    )

    pls.title('Line Plot: Automation Probability by Job Title')
    pls.xlabel('Job Title')
    pls.ylabel('Automation Probability (2030)')
    pls.xticks(rotation=100)
    pls.grid(True)
    pls.show()


def Bar_plot(psa):

    df = psa.sort_values(by='Risk_Category')

    pls.figure(figsize=(20, 15))
    pls.bar(
        df['Risk_Category'],
        df['Average_Salary'],
        color='blue'
    )

    pls.title('Bar Plot: Average Salary by Risk Category')
    pls.xlabel('Risk Category')
    pls.ylabel('Average Salary')
    pls.show()


def hist_plot(psa):

    pls.figure(figsize=(20, 15))
    pls.hist(
        psa['AI_Exposure_Index'],
        bins=6,
        color='green',
        edgecolor='black'
    )

    pls.title('Histogram: AI Exposure Index Distribution')
    pls.xlabel('AI Exposure Index')
    pls.ylabel('Number of Jobs')
    pls.show()
