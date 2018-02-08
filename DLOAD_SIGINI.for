
      
      
      SUBROUTINE DLOAD(F,KSTEP,KINC,TIME,NOEL,NPT,LAYER,KSPT,
     1 COORDS,JLTYP,SNAME)

      INCLUDE 'ABA_PARAM.INC'

      DIMENSION TIME(2), COORDS (3)
      CHARACTER*80 SNAME, stepnumber*10, direction*10
      CHARACTER*256 OUTDIR
      CHARACTER*256 JOBNAME
C      INTEGER*4 getcwd, status
C      character*255 dirname
      real :: R
      integer :: IP, flags
      CALL GETOUTDIR( OUTDIR, LENOUTDIR )
      CALL GETJOBNAME( JOBNAME, LENJOBNAME )
      IP = 4*(NOEL-1)+NPT 
      flag= 100+ (7-KSTEP)*3+JLTYP
      write(stepnumber, '(i1)') KSTEP
      write(direction, '(i1)') JLTYP
      if (IP.eq.1) then   
      OPEN(unit=flag,file=trim(OUTDIR)//'\force'//trim(direction)//
     1JOBNAME(14:14)//'.unf', form="unformatted", acc
     2ess="stream")
      else
         continue
      endif
      read(flag, POS=(IP*5 + (IP-1)*7)) R
      F = R 
C      write(7,*) NOEL,NPT,JLTYP,KSTEP,F,(IP*5 + (IP-1)*7),'s'//
C     1trim(direction)//trim(stepnumber)
      RETURN
      END
      
      SUBROUTINE SIGINI(SIGMA,COORDS,NTENS,NCRDS,NOEL,NPT,LAYER,
     1 KSPT,LREBAR,NAMES)
C
      INCLUDE 'ABA_PARAM.INC'
C
      DIMENSION SIGMA(NTENS),COORDS(NCRDS)
      CHARACTER NAMES(2)*80
      CHARACTER*256 OUTDIR
      CHARACTER*256 JOBNAME

      real :: R1, R2, R3, R4
      CALL GETOUTDIR( OUTDIR, LENOUTDIR ) 
      CALL GETJOBNAME( JOBNAME, LENJOBNAME )
      IP = 4*(NOEL-1)+NPT
      flag= 100+ (7-KSTEP)*4
      if (IP.eq.1) then   
      OPEN(unit=flag,file=trim(OUTDIR)//'\prestress1'//JOBNAME(14:14)
     1//'.unf', form="unformatted", access="stream")
      OPEN(unit=flag+1,file=trim(OUTDIR)//'\prestress2'//JOBNAME(14:14)
     1//'.unf', form="unformatted", access="stream")
      OPEN(unit=flag+2,file=trim(OUTDIR)//'\prestress3'//JOBNAME(14:14)
     1//'.unf', form="unformatted", access="stream")
      OPEN(unit=flag+3,file=trim(OUTDIR)//'\prestress4'//JOBNAME(14:14)
     1//'.unf', form="unformatted", access="stream")
      else
          continue
      endif
      read(flag,   POS=(IP*5 + (IP-1)*7)) R1
      read(flag+1, POS=(IP*5 + (IP-1)*7)) R2
      read(flag+2, POS=(IP*5 + (IP-1)*7)) R3
      read(flag+3, POS=(IP*5 + (IP-1)*7)) R4
      SIGMA(1) = R1
      SIGMA(2) = R2
      SIGMA(3) = R3
      SIGMA(4) = R4
      write(7,*) NTENS,NOEL,NPT,COORDS,SIGMA(1),SIGMA(2),SIGMA(4) 
      RETURN
      END
      
