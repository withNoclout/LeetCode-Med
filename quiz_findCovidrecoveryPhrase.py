import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, 
                                 covid_tests: pd.DataFrame) -> pd.DataFrame:
  
                    # We determine first positive per patient_id
    frstPos = (covid_tests[covid_tests.result == 'Positive']
        .groupby('patient_id').agg( Pos_date = ('test_date', 'min')).reset_index())
    df = covid_tests.merge(frstPos)

                    # We determine first negative test after first positive test
    frstNeg = (df[(df.test_date > df.Pos_date) & (df.result == 'Negative')]
        .groupby('patient_id').agg(Neg_date = ('test_date', 'min')).reset_index())
    df = frstPos.merge(frstNeg).dropna()

                    # We compute recovery time
    df['recovery_time'] = (pd.to_datetime(df.Neg_date) -
                           pd.to_datetime(df.Pos_date)).dt.days

                    # We merge patient info, sort rows and rearrange columns as directed
    df = df.merge(patients).sort_values(['recovery_time', 'patient_name'])
    return df.iloc[:,[0,4,5,3]]
