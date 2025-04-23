df["speedup"] = df["cpp_time_ns"] / df["rust_time_ns"]

# 4. Compute descriptive speedup: faster‐by‐how‐many‐times
def make_speedup(row):
    if row.faster_time == "C++":
        ratio = row.rust_time_ns / row.cpp_time_ns
        return f"C++ by {ratio:.2f}×"
    else:
        ratio = row.cpp_time_ns / row.rust_time_ns
        return f"Rust by {ratio:.2f}×"

df["speedup_desc"] = df.apply(make_speedup, axis=1)
