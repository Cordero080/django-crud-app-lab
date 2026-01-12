# CSS Architecture Decisions

## Overview

IronBody uses a monochromatic design system with CSS custom properties for maintainability.

## Design Decisions

### 1. CSS Custom Properties (Variables)

- All colors defined in `:root` for easy theming
- Semantic naming: `--fg`, `--fg-muted`, `--bg-dark`, `--bg-glass`
- Single source of truth for color palette

### 2. Simplified Selectors

- Removed redundant `!important` declarations where specificity suffices
- Combined similar selectors (e.g., `button, .btn`)
- Used inheritance where possible

### 3. Removed Dead Code

- Eliminated unused `.workout-card`, `.equipment-card` classes (using `main > div` instead)
- Removed redundant `box-sizing: border-box` on nav (inherited from `*`)
- Consolidated duplicate hover states

### 4. Glass Morphism Pattern

- Consistent `backdrop-filter: blur()` usage
- `-webkit-` prefix included for Safari support
- Standardized border opacity at `0.1` for subtle effect

### 5. Typography Scale

- h1: 2.5rem (hero)
- h2: 1.8rem (section)
- h3: inherits
- body: 1rem base
- Orbitron font throughout for futuristic feel

### 6. Spacing System

- Consistent padding: `0.75rem` inputs, `2rem` forms
- Gap utilities: `1rem`, `2.5rem` for flex containers
- Max-width: `900px` for content

### 7. Color Palette (Monochromatic)

```css
--fg: #ffffff           /* Primary text */
--fg-muted: rgba(255,255,255,0.7)  /* Secondary text */
--bg-dark: #0a0a0a      /* Background */
--accent: #666666       /* Subtle accent */
```

### 8. Transitions

- Standard: `0.2s ease` for most interactions
- Buttons: `0.3s ease` for more pronounced feedback

## File Structure

- Single stylesheet approach for simplicity
- Logical section ordering: Reset → Layout → Components → Utilities
