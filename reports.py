def show_record(r):
    print("\n--- SLUMP TEST REPORT ---")
    labels = [("Test ID","test_id"),("Date/time","date_time"),("Project","project"),
              ("Location","location"),("Batch/ticket","batch"),("Truck","truck"),
              ("Mix design","mix"),("Technician","technician"),
              ("Measured slump","slump_in"),("Specified minimum","minimum_in"),
              ("Specified maximum","maximum_in"),("Result","status"),("Notes","notes")]
    for label, key in labels:
        suffix = " in" if key in ("slump_in","minimum_in","maximum_in") else ""
        print(f"{label:20}: {r[key] or '-'}{suffix}")

def show_history(records):
    if not records:
        print("\nNo tests recorded yet.")
        return
    print(f"\n{'ID':8} {'DATE/TIME':25} {'PROJECT':20} {'BATCH':14} {'SLUMP':8} STATUS")
    print("-" * 95)
    for r in records:
        print(f"{r['test_id'][:8]:8} {r['date_time'][:25]:25} {r['project'][:20]:20} "
              f"{r['batch'][:14]:14} {r['slump_in']:>5}in  {r['status']}")
    passed = sum(r["status"] == "PASS" for r in records)
    print(f"\nTotal: {len(records)} | Pass: {passed} | Out of range: {len(records)-passed}")
