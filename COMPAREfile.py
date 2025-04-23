                                                                                      
import pandas as pd

# 1. Load both CSVs, renaming columns for clarity
cpp = (
    pd.read_csv("cpp_sensor_bench.csv")
      .rename(columns={"time_ns": "cpp_time_ns", "mem_kb": "cpp_mem_kb"})
)
rust = (
    pd.read_csv("../rust_sensors/rust_sensor_bench.csv")
      .rename(columns={"time_ns": "rust_time_ns", "mem_kb": "rust_mem_kb"})
)

# 2. Merge on sensor name
df = pd.merge(
    cpp[["sensor", "cpp_time_ns", "cpp_mem_kb"]],
    rust[["sensor", "rust_time_ns", "rust_mem_kb"]],
    on="sensor",
    how="inner",
)

# 3. Compute differences and labels
df["time_diff_ns"] = df["cpp_time_ns"] - df["rust_time_ns"]
df["faster_time"] = df.apply(
    lambda r: "C++" if r.cpp_time_ns < r.rust_time_ns else "Rust", axis=1
)

df["mem_diff_kb"] = df["cpp_mem_kb"] - df["rust_mem_kb"]
df["faster_memory"] = df.apply(
    lambda r: "C++" if r.cpp_mem_kb < r.rust_mem_kb else "Rust", axis=1
)
# 4. Compute speedup ratio (C++ time divided by Rust time)
def make_speedup(row):
    if row.faster_time == "C++":
        ratio = row.rust_time_ns / row.cpp_time_ns
        return f"C++ faster by {ratio:.2f}×"
    else:
        ratio = row.cpp_time_ns / row.rust_time_ns
        return f"Rust faster by {ratio:.2f}×"

df["speedup_desc"] = df.apply(make_speedup, axis=1)
# 5. Sort by absolute time difference (optional)
df = df.reindex(df["time_diff_ns"].abs().sort_values(ascending=False).index)

# 6. Print a Markdown table to the terminal
print(df.to_markdown(index=False))

# 7. Write out a full comparison CSV
df.to_csv("comparison_full.csv", index=False)
