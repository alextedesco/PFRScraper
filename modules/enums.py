# NFL Team dictionary with team abbreviation as keys and team name as the values
NFL_TEAMS = {
    'CRD': 'Cardinals',
    'ATL': 'Falcons',
    'RAV': 'Ravens',
    'BUF': 'Bills',
    'CAR': 'Panthers',
    'CHI': 'Bears',
    'CIN': 'Bengals',
    'CLE': 'Browns',
    'DAL': 'Cowboys',
    'DEN': 'Broncos',
    'DET': 'Lions',
    'GNB': 'Packers',
    'HTX': 'Texans',
    'CLT': 'Colts',
    'JAX': 'Jaguars',
    'KAN': 'Chiefs',
    'RAI': 'Raiders',
    'SDG': 'Chargers',
    'RAM': 'Rams',
    'MIA': 'Dolphins',
    'MIN': 'Vikings',
    'NWE': 'Patriots',
    'NOR': 'Saints',
    'NYG': 'Giants',
    'NYJ': 'Jets',
    'PHI': 'Eagles',
    'PIT': 'Steelers',
    'SFO': '49ers',
    'SEA': 'Seahawks',
    'TAM': 'Buccaneers',
    'OTI': 'Titans',
    'WAS': 'Commanders'
}

# Tuple that stores statistic name, abbreviation, link, and column number
OPTIONS = (
    ("Passes Completed", ("pass_cmp", "passing.htm#passing::", 7)),
    ("Passes Attempted", ("pass_att",  "passing.htm#passing::", 8)),
    ("Completion Percentage", ("pass_cmp_perc",  "passing.htm#passing::", 9)),
    ('Passing Yards', ('pass_yds',  "passing.htm#passing::", 10)),
    ('Passing Touchdowns', ('pass_td',  "passing.htm#passing::", 11)),
    ('Passing Interceptions', ('pass_int',  "passing.htm#passing::", 13)),
    ('Passer Rating', ('pass_rating',  "passing.htm#passing::", 22)),
    ('QBR', ('qbr', "passing.htm#passing::", 23))
)