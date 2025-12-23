# Security Policy

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in CryptoNoise-Ksampler, please report it responsibly.

### Do Not

- Do not open public GitHub issues for security vulnerabilities
- - Do not share vulnerability details publicly until a fix is available
  - - Do not disclose the vulnerability to other parties without permission
   
    - ### How to Report
   
    - Please report security vulnerabilities by email to the project maintainers. Include:
   
    - 1. **Description**: Clear description of the vulnerability
      2. 2. **Location**: File paths, line numbers, and functions affected
         3. 3. **Impact**: Potential impact of the vulnerability
            4. 4. **Reproduction**: Steps to reproduce the issue (if possible)
               5. 5. **Suggested Fix**: Any suggestions for fixing the issue (optional)
                 
                  6. ## Security Considerations
                 
                  7. ### Cryptographic Security
                 
                  8. CryptoNoise-Ksampler uses SHA-256 for cryptographic operations. The security of the system depends on:
                 
                  9. - **Secret Key Management**: Keep your `artist_key` confidential
                     - - **Collision Resistance**: SHA-256 is cryptographically secure (collision probability ~10^-77)
                       - - **Key Storage**: Store artist keys securely, never commit them to version control
                        
                         - ### Input Validation
                        
                         - All user inputs should be validated:
                         - - Artist keys should be strings of sufficient length
                           - - Generation parameters should match expected ranges
                             - - Seed values should be valid integers
                              
                               - ### Dependencies
                              
                               - We actively monitor dependencies for known vulnerabilities. If a vulnerability is discovered in a dependency:
                              
                               - 1. We will assess the impact
                                 2. 2. We will update the dependency or implement a workaround
                                    3. 3. We will release a security patch
                                      
                                       4. ## Supported Versions
                                      
                                       5. We provide security updates for:
                                      
                                       6. - **Current Version**: Latest release receives security patches
                                          - - **Previous Version**: Last major version receives critical patches
                                            - - **End of Life**: Versions older than 1 year may not receive patches
                                             
                                              - ## Security Best Practices
                                             
                                              - When using CryptoNoise-Ksampler:
                                             
                                              - 1. Keep your ComfyUI installation updated
                                                2. 2. Use strong, unique artist keys
                                                   3. 3. Protect your artist keys as you would any cryptographic secret
                                                      4. 4. Verify workflow integrity before running workflows from untrusted sources
                                                         5. 5. Keep Python and dependencies up to date
                                                           
                                                            6. ## Responsible Disclosure
                                                           
                                                            7. We follow responsible disclosure practices:
                                                           
                                                            8. - Security reports are addressed within 30 days
                                                               - - Fixes are developed and tested before disclosure
                                                                 - - Credit is given to researchers who report vulnerabilities responsibly
                                                                   - - Coordinated disclosure timeline will be agreed upon
                                                                    
                                                                     - ## Security Updates
                                                                    
                                                                     - Security patches will be released as soon as practical after a vulnerability is confirmed and fixed. Critical security vulnerabilities may be backported to previous versions.
                                                                    
                                                                     - ---

                                                                     **Thank you for helping keep CryptoNoise-Ksampler secure!**
