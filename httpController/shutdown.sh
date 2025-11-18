#!/usr/bin/env bash
#
# Notify HA about machine shutdown
# Actions: turn_off, turn_on, toggle
#
RESULT=$(curl -v POST \
              -H "Authorization: Bearer <TOKEN>" \
              -H "Content-Type: application/json" \
              -d '{"entity_id": "switch.destroyer_status"}' \
             'http://<HA.IP.ADDRESS>:8000/api/services/switch/turn_off')
logger "Shutdown in progress"
logger "$RESULT"
