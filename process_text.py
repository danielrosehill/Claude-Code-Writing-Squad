#!/usr/bin/env python3
"""
Claude Code Writing Squad - Text Processing Pipeline

This script processes text through a series of specialized editing agents,
each focusing on a specific aspect of writing improvement.

Usage:
    python process_text.py

The script reads from input.md and outputs to output.md, saving intermediate
results for review.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json


class AgentProcessor:
    """Handles the sequential processing of text through writing agents."""
    
    def __init__(self, base_dir=None):
        """Initialize the processor with the base directory."""
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent
        self.agents_dir = self.base_dir / "agents"
        self.input_file = self.base_dir / "input.md"
        self.output_file = self.base_dir / "output.md"
        self.intermediate_dir = self.base_dir / "intermediate"
        
        # Define the processing order
        self.agent_order = [
            "basic-typo-reviewer.md",
            "uk-english-standardiser.md", 
            "flow-and-polish.md",
            "headings.md",
            "proofreader.md",
            "add-sources.md",
            "seo-reviewer.md"
        ]
        
        # Agent display names for better output
        self.agent_names = {
            "basic-typo-reviewer.md": "Basic Typo Reviewer",
            "uk-english-standardiser.md": "UK English Standardiser",
            "flow-and-polish.md": "Flow and Polish",
            "headings.md": "Headings",
            "proofreader.md": "Proofreader", 
            "add-sources.md": "Add Sources",
            "seo-reviewer.md": "SEO Reviewer"
        }
    
    def load_agent_prompt(self, agent_file):
        """Load the prompt/instructions for a specific agent."""
        agent_path = self.agents_dir / agent_file
        if not agent_path.exists():
            raise FileNotFoundError(f"Agent configuration not found: {agent_path}")
        
        with open(agent_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    
    def load_input_text(self):
        """Load the input text to be processed."""
        if not self.input_file.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_file}")
        
        with open(self.input_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    
    def save_intermediate_result(self, agent_name, step_number, text):
        """Save intermediate processing results."""
        self.intermediate_dir.mkdir(exist_ok=True)
        
        # Clean filename
        clean_name = agent_name.replace(" ", "_").lower().replace("-", "_")
        filename = f"{step_number:02d}_{clean_name}.md"
        filepath = self.intermediate_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Step {step_number}: {agent_name}\n\n")
            f.write(f"*Processed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write("---\n\n")
            f.write(text)
        
        return filepath
    
    def save_final_output(self, text):
        """Save the final processed text."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Processed Output\n\n")
            f.write(f"*Final processing completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write("---\n\n")
            f.write(text)
    
    def create_processing_log(self, processing_steps):
        """Create a log of the processing steps."""
        log_file = self.base_dir / "processing_log.json"
        
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "input_file": str(self.input_file),
            "output_file": str(self.output_file),
            "processing_steps": processing_steps,
            "total_steps": len(processing_steps)
        }
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
        
        return log_file
    
    def simulate_agent_processing(self, agent_prompt, text):
        """
        Simulate agent processing.
        
        In a real implementation, this would send the text and prompt
        to Claude or another LLM for processing. For now, this is a
        placeholder that returns the text with a processing note.
        """
        # This is where you would integrate with Claude API or other LLM
        # For demonstration purposes, we'll just return the text with a note
        
        processed_text = f"{text}\n\n*[Note: This text would be processed by the agent in a real implementation]*"
        return processed_text
    
    def process_text(self):
        """Process the input text through all agents in sequence."""
        print("🚀 Starting Claude Code Writing Squad processing...")
        print(f"📁 Base directory: {self.base_dir}")
        print(f"📄 Input file: {self.input_file}")
        print(f"📄 Output file: {self.output_file}")
        print()
        
        # Load input text
        try:
            current_text = self.load_input_text()
            print(f"✅ Loaded input text ({len(current_text)} characters)")
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            print("💡 Please create an input.md file with your text to process.")
            return False
        
        processing_steps = []
        
        # Process through each agent
        for step_number, agent_file in enumerate(self.agent_order, 1):
            agent_name = self.agent_names[agent_file]
            print(f"\n📝 Step {step_number}: Processing with {agent_name}")
            
            try:
                # Load agent prompt
                agent_prompt = self.load_agent_prompt(agent_file)
                print(f"   ✅ Loaded agent configuration ({len(agent_prompt)} characters)")
                
                # Process text (this would be where you call Claude API)
                processed_text = self.simulate_agent_processing(agent_prompt, current_text)
                
                # Save intermediate result
                intermediate_file = self.save_intermediate_result(agent_name, step_number, processed_text)
                print(f"   💾 Saved intermediate result: {intermediate_file}")
                
                # Update current text for next agent
                current_text = processed_text
                
                # Log this step
                processing_steps.append({
                    "step": step_number,
                    "agent": agent_name,
                    "agent_file": agent_file,
                    "intermediate_file": str(intermediate_file),
                    "text_length": len(processed_text)
                })
                
            except Exception as e:
                print(f"   ❌ Error processing with {agent_name}: {e}")
                return False
        
        # Save final output
        self.save_final_output(current_text)
        print(f"\n✅ Final output saved: {self.output_file}")
        
        # Create processing log
        log_file = self.create_processing_log(processing_steps)
        print(f"📋 Processing log saved: {log_file}")
        
        print(f"\n🎉 Processing complete! Processed through {len(self.agent_order)} agents.")
        print(f"📊 Final text length: {len(current_text)} characters")
        print(f"📁 Intermediate files saved in: {self.intermediate_dir}")
        
        return True


def main():
    """Main entry point for the script."""
    print("Claude Code Writing Squad - Text Processing Pipeline")
    print("=" * 55)
    
    # Initialize processor
    processor = AgentProcessor()
    
    # Check if agents directory exists
    if not processor.agents_dir.exists():
        print(f"❌ Error: Agents directory not found: {processor.agents_dir}")
        sys.exit(1)
    
    # Check if all agent files exist
    missing_agents = []
    for agent_file in processor.agent_order:
        if not (processor.agents_dir / agent_file).exists():
            missing_agents.append(agent_file)
    
    if missing_agents:
        print(f"❌ Error: Missing agent configuration files:")
        for agent in missing_agents:
            print(f"   - {agent}")
        sys.exit(1)
    
    # Process the text
    success = processor.process_text()
    
    if success:
        print("\n💡 Next steps:")
        print("   1. Review the output.md file")
        print("   2. Check intermediate files to see progression")
        print("   3. Modify input.md and run again if needed")
        print("\n🔧 Note: This is a framework script. To use with actual LLM processing,")
        print("   integrate with Claude API or your preferred LLM service in the")
        print("   simulate_agent_processing() method.")
    else:
        print("\n❌ Processing failed. Please check the error messages above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
