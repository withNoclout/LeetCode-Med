class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        table_map = defaultdict(lambda: defaultdict(int))
        food_set = set()

        # Collect orders
        for _, table, food in orders:
            table = int(table)
            table_map[table][food] += 1
            food_set.add(food)

        # Sort food items and tables
        food_list = sorted(food_set)
        table_list = sorted(table_map.keys())

        # Build header row
        res = [["Table"] + food_list]

        # Fill table rows
        for table in table_list:
            row = [str(table)]
            for food in food_list:
                row.append(str(table_map[table][food]))
            res.append(row)

        return res
