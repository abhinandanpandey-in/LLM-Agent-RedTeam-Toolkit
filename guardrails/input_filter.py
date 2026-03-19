def layer_1_lexical_filter(user_input):
    """
    Layer 1: Lexical Command Override Detection
    Targets V1 and V2 patterns that explicitly invoke authority or attempt to cancel context.
    """
    override_keywords = ["ignore", "override", "bypass", "system", "diagnostic", "developer"]
    input_lower = user_input.lower()
    
    if any(keyword in input_lower for keyword in override_keywords):
        return False, "Blocked by Layer 1: Command override or diagnostic keyword detected."
    return True, "Pass"

def layer_2_entity_filter(user_input):
    """
    Layer 2: Protected Entity Recognition
    Targets V0 and partially constrains V3 when the target entity is named explicitly.
    """
    protected_entities = ["alice", "bob", "charlie"]
    input_lower = user_input.lower()
    
    # Simple regex-free matching for baseline implementation
    if any(entity in input_lower for entity in protected_entities):
        return False, "Blocked by Layer 2: Protected entity referenced directly."
    return True, "Pass"

def evaluate_guardrails(user_input):
    """
    Executes the two-layer pre-inference semantic filter.
    Returns True if safe, False if malicious.
    """
    passed_l1, reason_l1 = layer_1_lexical_filter(user_input)
    if not passed_l1:
        return False, reason_l1
        
    passed_l2, reason_l2 = layer_2_entity_filter(user_input)
    if not passed_l2:
        return False, reason_l2
        
    return True, "Input cleared by guardrails."