# This includes dynamically analyzed data from SQLite databases.
# Redundant information for visualization is contained.


class BtreeType:
    TABLE = "table"
    INDEX = "index"

class PageType:
    # FIRST_PAGE = "page#1"     # has db metadata
    TABLE_INTERIOR = "table interior page"
    TABLE_LEAF = "table leaf page"
    INDEX_INTERIOR = "index interior page"
    INDEX_LEAF = "index leaf page"
    OVERFLOW = "overflow page"
    UNCERTAIN = "uncertain page"


def get_dbinfo_template():
    """
    >>> dbinfo = get_dbinfo_template()
    >>> dbinfo['dbMetadata'] is not None
    True
    >>> dbinfo['pages'] is not None
    True
    >>> dbinfo['dbMetadata']['pageSize'] is not None
    True
    """
    return {
      "dbMetadata":
        {
          "pageSize": None, # UINT
          "nPages": None, # UINT
          "usablePageSize": None, # UINT
          "btrees":
            [
              # {
              #   "type": BtreeType.INDEX,
              #   "name": "idx_T0",
              #   "tableName": "T0",
              #   "rootPage": 8
              # },
              # ...
            ]
        },
      "pages":
        {
          # 1:  # Pages are read not always sequentially (ex: overflow page)
          #   {
          #     "pageMetadata":
          #       {
          #         "pageType": PageType.TABLE_LEAF,  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR, OVERFLOW]
          #         "nCells": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR, OVERFLOW]
          #         "freeBlockOffset": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR]
          #         "cellContentAreaOffset": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR]
          #         "nextOverflowPageNum": None, # UINT  [OVERFLOW]
          #         "livingBtree": "T0"  # One of ret["dbMetadata"]["btrees"]  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR, OVERFLOW]
          #         "rightmostChildPageNum": None, # UINT  [TABLE_INTERIOR, INDEX_INTERIOR]
          #       }
          #
          #     # Table leaf example:
          #     "cells":
          #       [
          #         {
          #           "offset": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR, OVERFLOW]
          #           "cellSize": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR, INDEX_LEAF, INDEX_INTERIOR, OVERFLOW]
          #           "leftChildPage": None, # UINT  [TABLE_INTERIOR, INDEX_INTERIOR]
          #           "rid": None, # UINT  [TABLE_LEAF, TABLE_INTERIOR]
          #           "overflowPage": None, # UINT  [TABLE_LEAF, INDEX_LEAF, INDEX_INTERIOR]
          #           "payload":  # TODO: Only size information is supported currently  [TABLE_LEAF, INDEX_LEAF, INDEX_INTERIOR]
          #             {
          #               "size": None, # UINT
          #               "offset": None, # UINT
          #               "headerSize": None, # UINT
          #               "bodySize": None, # UINT
          #             },
          #         },
          #         ...
          #       ]
          #   },
          # 2:
          #   ...
          # ...
        }
    }


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
