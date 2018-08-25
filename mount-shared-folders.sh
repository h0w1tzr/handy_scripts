#!/bin/bash

sudo vmware-hgfsclient | while read folder; do
  echo "[i] Mounting ${folder}   (/mnt/hgfs/${folder})"
  sudo mkdir -p "/mnt/hgfs/${folder}"
  sudo umount -f "/mnt/hgfs/${folder}" 2>/dev/null
  sudo vmhgfs-fuse -o allow_other -o auto_unmount ".host:/${folder}" "/mnt/hgfs/${folder}"
done

sleep 2s
