import numpy as np

lw1_sql_content = np.array(['ON', 'OFF'])
lw2_sql_content = np.array(['OFF', 'ON'])

comparison = lw1_sql_content == lw2_sql_content
are_equal  = comparison.all()

print(comparison.all())


