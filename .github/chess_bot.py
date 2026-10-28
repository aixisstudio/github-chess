import os, re, chess, random, pathlib, json, datetime
EVENT = json.load(open(os.environ["GITHUB_EVENT_PATH"]))
issue = EVENT["issue"]; user = issue["user"]["login"]
title = issue["title"].strip().lower()
state = pathlib.Path("game"); state.mkdir(exist_ok=True)
fenf = state/"state.fen"
board = chess.Board(fenf.read_text().strip() if fenf.exists() else chess.STARTING_FEN)
mv = re.sub(r"^(move[: ]+)","", title)
com = pathlib.Path("comment.md")
def bot_move(b):
    # greedy: mate > capture (highest victim) > develop > random
    legal = list(b.legal_moves)
    mates = [m for m in legal if b.gives_check(m)]
    for m in mates:
        b.push(m)
        if b.is_checkmate(): b.pop(); return m
        b.pop()
    caps = sorted([m for m in legal if b.is_capture(m)],
                  key=lambda m: (b.piece_type_at(m.to_square) or 0)*10 - (b.piece_type_at(m.from_square) or 0), reverse=True)
    if caps and random.random() < 0.8: return caps[0]
    return random.choice(legal)
if mv == "resign":
    res = "1-0" if board.turn == chess.BLACK else "0-1"
    com.write_text(f"🏳️ @{user} resigns. Result: **{res}**. Start a new game with `new`!")
elif mv == "new":
    board = chess.Board()
    com.write_text(f"♟️ New game started by @{user}! Open an issue with your move (e.g. `e2e4`).")
else:
    try:
        m = board.parse_san(mv) if not re.match(r"^[a-h][1-8][a-h][1-8][qrbn]?$", mv) else chess.Move.from_uci(mv)
        if m not in board.legal_moves: raise ValueError
    except Exception:
        com.write_text(f"❌ `{mv}` is not a legal move, @{user}. Use SAN (`Nf3`, `O-O`) or UCI (`e2e4`).")
        print("illegal"); raise SystemExit(0)
    san = board.san(m); board.push(m)
    reply = ""
    if board.is_game_over():
        res = board.result(); reply = f" Game over: **{res}**!"
    else:
        bm = bot_move(board); bsan = board.san(bm); board.push(bm)
        reply = f" Bot replies **{bsan}**."
    com.write_text(f"✅ @{user} played **{san}**.{reply}")
    # log
    with open(state/"moves.csv","a") as f: f.write(f"{user},{san},{datetime.date.today()}\n")
    # players board
    pf = state/"players.md"
    lines = pf.read_text().splitlines() if pf.exists() else ["# 🏆 Players","", "| Player | Moves |","|---|---|"]
    rows = {l.split("|")[1].strip(): int(l.split("|")[2].strip()) for l in lines[3:] if l.startswith("|") and "---" not in l and l.split("|")[2].strip().isdigit()}
    rows[user] = rows.get(user,0)+1
    pf.write_text("\n".join(lines[:3]+[f"| {u} | {n} |" for u,n in sorted(rows.items(),key=lambda x:-x[1])])+"\n")
fenf.write_text(board.fen())
# render board
ICONS = {"r":"♜","n":"♞","b":"♝","q":"♛","k":"♚","p":"♟","R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔","P":"♙"}
rows = []
for r in range(8):
    row = f"{8-r} "
    for c in range(8):
        sq = board.piece_at(chess.square(c, 7-r))
        row += ICONS.get(sq.symbol(),"·") if sq else "·"
        row += " "
    rows.append(row)
rows.append("  a b c d e f g h")
turn = "⚪ White" if board.turn else "⚫ Black"
(state/"board.md").write_text("```\n"+"\n".join(rows)+"\n```\n\n**Turn:** "+turn+"\n")
print("ok")
