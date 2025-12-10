import streamlit as st
import random
from typing import List, Optional, Tuple

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Add simple animations for buttons
st.markdown("""
<style>
button[kind="primary"] {
    transition: transform 0.1s ease-in-out !important;
}
button[kind="primary"]:active {
    transform: scale(0.90) !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Game Logic
# -----------------------
WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

def new_board():
    return [""] * 9

def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(board):
        return "Draw"
    return None

def available_moves(board):
    return [i for i, v in enumerate(board) if not v]

def opposite(player):
    return "O" if player == "X" else "X"

def make_move(board, idx, player):
    board[idx] = player


# Minimax AI
def minimax(board, player, maximizing):
    winner = check_winner(board)
    if winner == "X": return 1, None
    if winner == "O": return -1, None
    if winner == "Draw": return 0, None

    moves = available_moves(board)
    best_move = None

    if maximizing:
        best_score = -999
        for m in moves:
            board[m] = player
            score, _ = minimax(board, opposite(player), False)
            board[m] = ""
            if score > best_score:
                best_score = score
                best_move = m
        return best_score, best_move
    else:
        best_score = 999
        for m in moves:
            board[m] = player
            score, _ = minimax(board, opposite(player), True)
            board[m] = ""
            if score < best_score:
                best_score = score
                best_move = m
        return best_score, best_move

def ai_move(board, ai_mark, difficulty):
    moves = available_moves(board)
    if not moves:
        return None
    if difficulty == "Easy":
        return random.choice(moves)
    maximizing = ai_mark == "X"
    _, best = minimax(board, ai_mark, maximizing)
    return best if best is not None else random.choice(moves)

# -----------------------
# Session State
# -----------------------
if "board" not in st.session_state:
    st.session_state.board = new_board()
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Flags to ensure we process win/animations exactly once
if "winner_processed" not in st.session_state:
    st.session_state.winner_processed = False
if "animation_played" not in st.session_state:
    st.session_state.animation_played = False

# Scoreboard
if "score_x" not in st.session_state:
    st.session_state.score_x = 0
if "score_o" not in st.session_state:
    st.session_state.score_o = 0
if "score_draw" not in st.session_state:
    st.session_state.score_draw = 0

# -----------------------
# Reset Function
# -----------------------
def reset_game(start="X"):
    st.session_state.board = new_board()
    st.session_state.turn = start
    st.session_state.winner = None
    st.session_state.winner_processed = False
    st.session_state.animation_played = False

# -----------------------
# Sidebar Options
# -----------------------
st.sidebar.header("Game Settings")
player_x = st.sidebar.text_input("Player X name", "Player X")
player_o = st.sidebar.text_input("Player O name", "Player O")

vs_cpu = st.sidebar.checkbox("Play vs Computer", value=False)
cpu_mark = st.sidebar.selectbox("Computer plays as", ["O", "X"])
difficulty = st.sidebar.radio("AI difficulty", ["Easy", "Hard"])

if st.sidebar.button("Reset Scoreboard"):
    st.session_state.score_x = 0
    st.session_state.score_o = 0
    st.session_state.score_draw = 0
    # Keep the current game but allow animations again if needed later
    st.session_state.winner_processed = False
    st.session_state.animation_played = False
    st.toast("Scoreboard reset!", icon="🧹")

# -----------------------
# Title + Scoreboard Display
# -----------------------
st.title("🎮 Tic-Tac-Toe")

st.subheader("Scoreboard")
score_cols = st.columns(3)
score_cols[0].metric("X Wins", st.session_state.score_x)
score_cols[1].metric("O Wins", st.session_state.score_o)
score_cols[2].metric("Draws", st.session_state.score_draw)

board = st.session_state.board

# -----------------------
# Handle Button Press
# -----------------------
def on_click(i):
    # Don't allow moves after there's a winner
    if st.session_state.winner:
        return
    if board[i] != "":
        return
    # If it's CPU's turn, human shouldn't be able to click
    if vs_cpu and st.session_state.turn == cpu_mark:
        return

    # Human move
    make_move(board, i, st.session_state.turn)
    st.session_state.winner = check_winner(board)

    # If game ended, don't switch turn
    if st.session_state.winner:
        return

    st.session_state.turn = opposite(st.session_state.turn)

# -----------------------
# Display Board (stable keys)
# -----------------------
for row in range(3):
    columns = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        label = board[idx] or " "
        key = f"c{idx}"
        if columns[col].button(label, key=key):
            on_click(idx)

# -----------------------
# AI Auto-Move
# -----------------------
# Important: run AI move only when there is no winner and it's CPU's turn
if vs_cpu and st.session_state.winner is None and st.session_state.turn == cpu_mark:
    ai_idx = ai_move(board, cpu_mark, difficulty)
    if ai_idx is not None:
        make_move(board, ai_idx, cpu_mark)
        st.session_state.winner = check_winner(board)
        if st.session_state.winner is None:
            st.session_state.turn = opposite(st.session_state.turn)

# -----------------------
# Winner / Draw Logic + Animations (processed once)
# -----------------------
winner = st.session_state.winner

# If winner exists and we haven't processed it yet -> update scoreboard and play animations.
if winner and not st.session_state.winner_processed:

    # Update scoreboard
    if winner == "X":
        st.session_state.score_x += 1
    elif winner == "O":
        st.session_state.score_o += 1
    else:
        st.session_state.score_draw += 1

    # Play animations once (set animation_played so it's not replayed on reruns)
    if not st.session_state.animation_played:
        if winner in ("X", "O"):
            st.balloons()
            st.toast(f"{player_x if winner=='X' else player_o} wins! 🎉")
        else:
            st.snow()
            st.toast("It's a draw! 🤝")
        st.session_state.animation_played = True

    # Mark processed so toggling sidebar options won't increment scores again
    st.session_state.winner_processed = True

    # Stop here to avoid intermediate reruns canceling animations
    st.stop()

# Clean result display (no ternary that returns None)
if winner:
    st.success(f"Result: {winner}")

# -----------------------
# Reset Buttons
# -----------------------
st.write("---")
btns = st.columns(2)
if btns[0].button("🔄 Restart (X starts)"):
    reset_game("X")
if btns[1].button("🔁 Restart (O starts)"):
    reset_game("O")
