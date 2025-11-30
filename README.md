# 🏥 Clinical Data Processor

A secure and user-friendly desktop application for managing clinical trial data files through FTP connections. Built with Python and Tkinter, featuring comprehensive file validation, automated processing, and modern UI design principles.

## 📋 Features

### 🔐 Secure FTP Integration
- Connect to FTP servers with secure authentication
- Browse and manage remote CSV files
- Download files with automatic date-based naming

### ✅ Smart File Validation
- **Filename Pattern Validation**: Ensures files follow `CLINICALDATA{timestamp}.CSV` format
- **Content Validation**: 
  - Header structure verification
  - Data type validation (dosage, dates)
  - Business logic checks (end dates after start dates)
  - Duplicate record detection
- **Outcome Validation**: Validates clinical outcomes against predefined values

### 📊 Advanced Error Handling
- **Decorator Pattern Implementation**: Enhanced error logging with:
  - Timestamps for tracking
  - Unique GUIDs for error identification
  - File context for debugging
- Comprehensive error reporting and logging

 🎨 Modern User Interface
- Clean, intuitive design following established HCI principles
- Real-time progress tracking
- Multi-tab logging system
- Responsive layout with visual feedback

## 🧪 Testing Strategy

### Test-Driven Development (TDD) Approach
Our development followed the Red-Green-Refactor cycle:

### Nielsen's 10 Usability Heuristics Applied
✅ Visibility of System Status

Real-time progress bars and status labels

Connection status indicators

Operation completion notifications

✅ Match Between System and Real World

Medical domain terminology (PatientID, TrialCode, Dosage_mg)

Familiar file management metaphors

✅ User Control and Freedom

Cancel operations at any time

Undo/redo capabilities

Clear navigation between functions

✅ Consistency and Standards

Uniform button styles and colors

Consistent layout across all panels

Standard error message formats

✅ Error Prevention

Input validation before processing

Confirmation dialogs for destructive actions

Constrained choices where appropriate

✅ Recognition Rather Than Recall

Visual file status indicators (✅/❌)

Persistent log history

Clear action button labels

✅ Flexibility and Efficiency of Use

Keyboard shortcuts for power users

Bulk operations capability

Search and filter functionality

✅ Aesthetic and Minimalist Design

Clean, uncluttered interface

Logical information grouping

Progressive disclosure of complex features

✅ Help Users Recognize, Diagnose, and Recover from Errors

Detailed error messages with context

Suggested recovery actions

Comprehensive error logging

✅ Help and Documentation

Built-in help system

Tooltips and guidance

Clear operation instructions

Shneiderman's Eight Golden Rules Implemented
✅ Strive for Consistency

Uniform color scheme and typography

Consistent button placement and behavior

Standardized error message formats

✅ Enable Frequent Users to Use Shortcuts

Quick access to common functions

Keyboard navigation support

Batch processing capabilities

✅ Offer Informative Feedback

Real-time operation status

Progress indicators for long operations

Success/error notifications with details

✅ Design Dialogs to Yield Closure

Clear start-process-end workflows

Completion confirmation messages

Summary reports after processing

✅ Offer Error Prevention and Simple Error Handling

Proactive validation before submission

Clear error messages with solutions

Graceful recovery from failures

✅ Permit Easy Reversal of Actions

Cancel operations mid-process

Clear separation between validation and processing

Safe file handling with backups

✅ Support Internal Locus of Control

Users initiate all actions

Clear cause-effect relationships

Predictable system behavior

✅ Reduce Short-Term Memory Load

Persistent file lists and logs

Visual status indicators

Context-preserving navigation

🛠️ Technical Architecture
Design Patterns Used
Decorator Pattern: Enhanced error handling with timestamp, GUID, and context

Factory Pattern: Error handler creation

Observer Pattern: Event-driven UI updates


#### 🔴 RED Stage
```python
# Example failing test
def test_filename_validation_should_fail():
    validator = ClinicalDataValidator("/tmp", "/tmp", "/tmp")
    result = validator._validate_filename_pattern("CLINICALDATA20251111083303.csv")
    assert result == True  # Initially fails when code is broken
```

#### Core Components
```
ClinicalDataProcessor    # FTP operations and file management
ClinicalDataValidator    # Validation logic and error handling
ClinicalDataGUI          # Modern Tkinter interface
ErrorHandler             # Decorator-based error management
```

####  Project Structure
```
clinical-data-processor/
├── helix_softavalon.py          # Main application
├── test_validator.py            # Validation tests
├── README.md                    # This file
```


