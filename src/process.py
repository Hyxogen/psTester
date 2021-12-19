# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    process.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/16 15:40:55 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 16:15:58 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import asyncio


async def ExecuteProcess(path: str, args: list, sem):
	async with sem:
		proc = await asyncio.create_subprocess_exec(path, *args, stdin=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
		await proc.wait()
		return proc.returncode, proc.stdout, proc.stderr
