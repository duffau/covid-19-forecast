import pandas as pd
import random
import data_prep.fuzzy_merge.fuzzy_merge as fuzz

COUNTRIES_1 = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'DR Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar',
               'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea',
               'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of the Congo', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthélemy', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
               'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
COUNTRIES_2 = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Arab World', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon',
               'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, Dem. People’s Rep.', 'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Least developed countries: UN classification', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
               'North America', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'OECD members', 'Oman', 'Other small states', 'Pacific island small states', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Post-demographic dividend', 'Pre-demographic dividend', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Small states', 'Solomon Islands', 'Somalia', 'South Africa', 'South Asia', 'South Asia (IDA & IBRD)', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
               'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Upper middle income', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']


def test_fuzzy_merge_all_matches():
    left = pd.DataFrame({'key': ['abc', 'def', 'xyz'], 'value_left': [1, 1, 1]})
    right = pd.DataFrame({'key': ['abc', 'def', 'xyz'], 'value_right': [2, 2, 2]})
    df = fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='key', right_on='key')
    assert (df.key == left.key).all(), print(df)
    assert (df.key == right.key).all(), print(df)
    assert sum(df.value_left.isna()) == 0
    assert sum(df.value_right.isna()) == 0


def test_fuzzy_merge_one_mismatch():
    left = pd.DataFrame({'key': ['abc', 'def', 'xyz'], 'value_left': [1] * 3})
    right = pd.DataFrame({'key': ['abc', 'def', 'lmn'], 'value_right': [2] * 3})
    df = fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='key', right_on='key', suffixes=('_left', '_right'))
    assert (df.key == left.key).all(), f'{str(df)}\n{df.info()}'
    assert not (df.key == right.key).all(), f'{str(df)}\n{df.info()}'
    assert sum(df.value_left.isna()) == 0
    assert sum(df.value_right.isna()) == 1


def test_fuzzy_merge_one_close_match():
    left = pd.DataFrame({'key': ['abc', 'def', 'xyz'], 'value_left': [1] * 3})
    right = pd.DataFrame({'key': ['abc', 'def', 'xyzz'], 'value_right': [2] * 3})
    df = fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='key', right_on='key', threshold=80, suffixes=('_left', '_right'))
    assert (df.key == left.key).all(), print(df)
    assert sum(df.value_left.isna()) == 0
    assert sum(df.value_right.isna()) == 0


def test_fuzzy_merge_different_size_all_match():
    left = pd.DataFrame({'key': ['abc', 'def', 'xyz'] * 3, 'value_left': [1] * 3 * 3})
    right = pd.DataFrame({'key': ['abc', 'def', 'xyz'], 'value_right': [2] * 3})
    df = fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='key', right_on='key', suffixes=('_left', '_right'))
    assert (df.key == left.key).all(), print(df)
    assert set(df.key) == set(right.key), print(df)
    assert sum(df.value_left.isna()) == 0
    assert sum(df.value_right.isna()) == 0


def test_fuzzy_merge_different_close_all_match():
    left = pd.DataFrame({'key': ['abc', 'def', 'xyz'] * 3, 'value_left': [1] * 3 * 3})
    right = pd.DataFrame({'key': ['abc', 'def', 'xxyz'], 'value_right': [2] * 3})
    df = fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='key', right_on='key', threshold=80, suffixes=('_left', '_right'))
    assert (df.key == left.key).all(), print(df)
    assert sum(df.value_left.isna()) == 0
    assert sum(df.value_right.isna()) == 0



def test_fuzzy_merge_big_data():
    """Big data set smoke test for speed comparisons. Use with pytest flag --durations=0"""

    left = pd.DataFrame({
            'country': COUNTRIES_1,
            'x_values': [random.uniform(0, 1) for _ in range(len(COUNTRIES_1))]
        }
    )

    right = pd.DataFrame({
            'country': COUNTRIES_2,
            'y_values': [random.uniform(0, 1) for _ in range(len(COUNTRIES_2))]
        }
    )

    fuzz.fuzzy_left_merge(left.copy(), right.copy(), left_on='country', right_on='country')
