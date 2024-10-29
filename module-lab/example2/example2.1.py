def lead_safe(lead, has_ball, seconds_left):
    adjusted_lead = lead - 3  # Subtract 3 from the lead
    if has_ball:
        adjusted_lead += 0.5  # Add 0.5 if the team has possession
    else:
        adjusted_lead -= 0.5  # Subtract 0.5 if they don't
    adjusted_lead = adjusted_lead ** 2  # Square the result

    if adjusted_lead > seconds_left:
        return "The lead is safe."
    else:
        return "The lead is not safe."

# Example usage
print(lead_safe(2, True, 60))  # Expected: The lead is safe
