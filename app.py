import os
import sys

import caravan_pathfinder

pathfinder_broker_url = os.getenv('PATHFINDER_BROKER_URL')
if pathfinder_broker_url is None:
    print('PATHFINDER_BROKER_URL not provided')
    sys.exit(-1)

pathfinder_port = os.getenv('PATHFINDER_PORT', 1984)
pathfinder_broker_queue = os.getenv('PATHFINDER_BROKER_QUEUE', 'sparkhara')

caravan_pathfinder.main(pathfinder_broker_url,
                        pathfinder_port,
                        pathfinder_broker_queue)
